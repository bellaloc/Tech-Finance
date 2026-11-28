"""Regression tests for malformed CSV input and chronological forecast isolation."""
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

from evaluation.backtest import load_prices, evaluate
from evaluation.walk_forward import walk_forward


class DataIntegrityTests(unittest.TestCase):
    def test_invalid_csv(self):
        cases = (
            "date,value\n2024-01-01,10\n",
            "date,price\n2024-01-01,nan\n",
            "date,price\n2024-01-01,inf\n",
            "date,price\n2024-01-01,0\n",
            "date,price\n2024-01-01,10\n2024-01-01,11\n",
            "date,price\n2024-01-02,10\n2024-01-01,11\n",
            "date,price\nnot-a-date,10\n",
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "prices.csv"
            for content in cases:
                with self.subTest(content=content):
                    path.write_text(content, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        load_prices(path)

    def test_future_prices_do_not_change_earlier_forecasts(self):
        rows = [(date(2024, 1, 1) + timedelta(days=i), 100.0 + i)
                for i in range(50)]
        changed = rows[:-1] + [(rows[-1][0], 9999.0)]
        for benchmark in (evaluate, walk_forward):
            with self.subTest(benchmark=benchmark.__name__):
                original = benchmark(rows)
                modified = benchmark(changed)
                self.assertEqual(original["window"], modified["window"])
                self.assertEqual(original["predictions"][:-1],
                                 modified["predictions"][:-1])
                for key in original["metrics"]:
                    self.assertEqual(original["predictions"][-1][key],
                                     modified["predictions"][-1][key])
                self.assertNotEqual(original["predictions"][-1]["actual"],
                                    modified["predictions"][-1]["actual"])

    def test_linear_series_has_zero_regression_error(self):
        rows = [(date(2024, 1, 1) + timedelta(days=i), 100.0 + 2*i)
                for i in range(50)]
        result = walk_forward(rows)
        self.assertAlmostEqual(result["metrics"]["linear_regression"]["mae"], 0)
        self.assertAlmostEqual(result["metrics"]["persistence"]["mae"], 2)
        self.assertEqual(result["test_count"], 10)
