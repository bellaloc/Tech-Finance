import unittest
from datetime import date, timedelta
from pathlib import Path
from tempfile import TemporaryDirectory
from evaluation.backtest import evaluate, load_prices


class BacktestTests(unittest.TestCase):
    def setUp(self):
        self.rows = [(date(2024, 1, 1) + timedelta(days=i), 100 + i)
                     for i in range(10)]

    def test_known_baselines(self):
        result = evaluate(self.rows)
        self.assertEqual(result["train_count"], 6)
        self.assertEqual(result["test_count"], 4)
        self.assertEqual(result["metrics"]["persistence"]["mae"], 1)
        self.assertEqual(result["metrics"]["moving_average"]["rmse"], 2)

    def test_future_values_do_not_change_prior_predictions(self):
        before = evaluate(self.rows)["predictions"]
        changed = self.rows[:8] + [(d, 999) for d, _ in self.rows[8:]]
        after = evaluate(changed)["predictions"]
        for a, b in zip(before[:3], after[:3]):
            self.assertEqual(a["persistence"], b["persistence"])
            self.assertEqual(a["moving_average"], b["moving_average"])

    def test_insufficient_data(self):
        with self.assertRaises(ValueError):
            evaluate(self.rows[:3])

    def test_invalid_csv(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "prices.csv"
            for body in ("date,price\n2024-01-01,nan\n",
                         "date,price\n2024-01-01,10\n2024-01-01,11\n"):
                path.write_text(body)
                with self.assertRaises(ValueError):
                    load_prices(path)


if __name__ == "__main__":
    unittest.main()
