"""Chronological one-step price forecasts; no trading or return claims."""
import csv
import math
from datetime import date
from pathlib import Path
from statistics import mean


def load_prices(path):
    with Path(path).open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if not {"date", "price"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain date and price columns")
        rows = [(date.fromisoformat(r["date"]), float(r["price"])) for r in reader]
    if any(not math.isfinite(p) or p <= 0 for _, p in rows):
        raise ValueError("Prices must be positive and finite")
    if any(a[0] >= b[0] for a, b in zip(rows, rows[1:])):
        raise ValueError("Dates must be unique and strictly increasing")
    return rows


def evaluate(rows, window=3, holdout=0.4):
    """Fixed holdout, rolling observed history, persistence vs mean baseline."""
    if window < 2 or not 0 < holdout < 1:
        raise ValueError("Invalid window or holdout")
    split = max(window, int(len(rows) * (1 - holdout)))
    if split >= len(rows):
        raise ValueError("Not enough observations for evaluation")
    prices = [p for _, p in rows]
    predictions = []
    for i in range(split, len(rows)):
        predictions.append({
            "date": rows[i][0].isoformat(),
            "actual": prices[i],
            "persistence": prices[i - 1],
            "moving_average": mean(prices[i-window:i]),
        })
    metrics = {}
    for model in ("persistence", "moving_average"):
        errors = [r[model] - r["actual"] for r in predictions]
        metrics[model] = {"mae": mean(map(abs, errors)),
                          "rmse": math.sqrt(mean(e * e for e in errors))}
    return {"train_count": split, "test_count": len(predictions),
            "window": window, "predictions": predictions, "metrics": metrics}
