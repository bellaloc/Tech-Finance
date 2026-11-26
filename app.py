"""Read-only demonstration dashboard; no live market or trading claims."""
from pathlib import Path
from flask import Flask, render_template, request
from evaluation.backtest import load_prices, evaluate

ROOT = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=str(ROOT / "deployment/app/templates"))

@app.get("/")
def index():
    try:
        window = int(request.args.get("window", "3"))
        if window not in (2, 3, 5):
            raise ValueError("Choose a window of 2, 3 or 5 observations.")
        result = evaluate(load_prices(ROOT / "data/demo_prices.csv"), window=window)
    except (ValueError, OSError):
        return render_template("index.html", error="Unable to evaluate the demo. Choose a valid window or try again later.", result=None, window=3), 400
    return render_template("index.html", result=result, window=window, error=None)

if __name__ == "__main__":
    app.run()
