"""Independent chronological validation and test for one-step price forecasts."""
import math
from statistics import mean


def _linear(history):
    n = len(history)
    center = (n - 1) / 2
    average = mean(history)
    slope = sum((i - center) * (p - average) for i, p in enumerate(history))
    slope /= sum((i - center) ** 2 for i in range(n))
    return average + slope * (n - center)


def walk_forward(rows, windows=(3, 5, 10)):
    """Select regression window on validation only; compare on untouched test."""
    windows = tuple(sorted(set(windows)))
    if not windows or any(type(w) is not int or w < 2 for w in windows):
        raise ValueError("Windows must be integers >= 2")
    prices = [p for _, p in rows]
    if any(not math.isfinite(p) or p <= 0 for p in prices):
        raise ValueError("Prices must be positive and finite")
    if any(a[0] >= b[0] for a, b in zip(rows, rows[1:])):
        raise ValueError("Dates must be strictly increasing")
    train_end, validation_end = len(rows) * 3 // 5, len(rows) * 4 // 5
    if train_end < max(windows) or not train_end < validation_end < len(rows):
        raise ValueError("Insufficient observations for train/validation/test")
    scores = {w: mean(abs(_linear(prices[i-w:i]) - prices[i])
                      for i in range(train_end, validation_end)) for w in windows}
    window = min(windows, key=lambda w: (scores[w], w))
    predictions = [{"date": rows[i][0].isoformat(), "actual": prices[i],
                    "persistence": prices[i-1],
                    "moving_average": mean(prices[i-window:i]),
                    "linear_regression": _linear(prices[i-window:i])}
                   for i in range(validation_end, len(rows))]
    metrics = {}
    for model in ("persistence", "moving_average", "linear_regression"):
        errors = [r[model] - r["actual"] for r in predictions]
        metrics[model] = {"mae": mean(map(abs, errors)),
                          "rmse": math.sqrt(mean(e*e for e in errors))}
    return {"train_count": train_end, "validation_count": validation_end-train_end,
            "test_count": len(predictions), "window": window,
            "validation_mae": scores, "predictions": predictions, "metrics": metrics}
