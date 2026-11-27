# Tech-Finance

Christa Lococo — educational forecast evaluation lab. Not investment advice, live trading, or a validated stock predictor.

## Run the dashboard

From the repository root, with Python 3.12:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-web.txt
python -m unittest discover -s tests -v
python app.py
```

Open http://127.0.0.1:5000. The read-only dashboard supports moving-average window selection (2, 3 or 5 observations), toggling chart series, accessible tabular results and invalid-input handling. No external chart service or API key is required. The bundled data/demo_prices.csv contains 20 deliberately synthetic daily observations, not actual trading dates or market prices.

## Evaluation

CSV inputs require ascending unique ISO dates and positive finite prices. The last 40% of observations form a chronological holdout (with enough initial observations for the selected window). Persistence and trailing moving average use only observed history before each forecast. MAE and RMSE measure one-step price error, not returns. The window selector is educational; selecting a model on holdout results would invalidate an independent final evaluation.

For real historical evaluation, use a locally obtained CSV that you have permission to use. Do not commit or redistribute restricted market data. Record the provider URL, symbol, retrieval date, frequency, currency, adjustment policy, date range and SHA-256 of the original and normalized files. Normalize to `date,price`, omit missing observations explicitly, and keep actual trading dates (do not forward-fill holidays). Place the normalized file outside this repository. The command below expects that file; no historical results have been verified yet.
```sh
python -c "from evaluation.backtest import load_prices,evaluate; print(evaluate(load_prices('../historical_prices.csv')))"
```

## Independent regression benchmark

For a separate 60/20/20 chronological train/validation/test evaluation, use the rolling linear regression benchmark. It selects a trailing window (3, 5 or 10 observations) by validation MAE, freezes that choice, and compares regression, persistence and moving average on the same final test dates. Each forecast uses only previously observed prices. At least 17 observations are required with default windows; use substantially more for meaningful evaluation.

```sh
python -c "from evaluation.backtest import load_prices; from evaluation.walk_forward import walk_forward; print(walk_forward(load_prices('../historical_prices.csv')))"
```

This is an offline benchmark, not yet integrated into the dashboard. Synthetic tests verify mechanics, not market predictive ability. Do not tune against the final test or interpret price error as trading profitability.

## Deployment and limitations

Use requirements-web.txt for the dashboard, not the legacy requirements.txt. A production WSGI host must import app:app, use Python 3.12, and install a supported WSGI server; Flask's development server is local only. Production deployment requires passing build, tests, security review and readiness checks; none has been verified. Preview hosting, browser interaction verification, dependency locking/security audit, historical data provenance and historical regression results remain outstanding. Legacy scripts and dependencies are not validated and are not imported by the dashboard. The original README mentioned MIT but no LICENSE file was found; confirm intended license before redistribution.
