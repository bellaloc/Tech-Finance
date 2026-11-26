# Tech Finance Project

Christa Lococo

An experimental financial-data analysis project. This is not investment advice,
a live trading system, or a validated investment predictor.

## Implemented in this branch

- Dependency-free CSV validation and chronological one-step forecast evaluation.
- Persistence (last observed price) and trailing moving-average baselines.
- MAE and RMSE on a fixed chronological holdout, with observed history updated
  after each prediction. No future observations enter a prediction.
- Unit tests for known errors, future-data isolation and invalid inputs.

Run from the repository root with Python 3.12:

```sh
python -m unittest discover -s tests -v
python -c "from evaluation.backtest import load_prices,evaluate; print(evaluate(load_prices('data/raw_data/raw_data.csv')))"
```

The repository's sample generator produces synthetic prices for ten dates in
January 2022. Treat bundled data as demo data unless provenance is independently
established. For historical evaluation, supply a CSV with documented source,
symbol, adjustment policy and dates, using columns date,price in ascending order.
No market performance, profitability or predictive advantage is claimed.

## Existing prototype and remaining work

The legacy Flask application, model scripts and requirements remain for review;
the web interface is not verified, dependencies are outdated and its template
path needs repair. Interactive charts, historical dataset provenance, model
comparison beyond baselines, dependency/security updates and deployment are
pending. No production deployment is authorized by this branch.

The original README described an MIT license, but no LICENSE file was found in
the repository tree; confirm the intended license before redistribution.
