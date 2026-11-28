import unittest
from datetime import date, timedelta
from evaluation.walk_forward import walk_forward


class WalkForwardTests(unittest.TestCase):
    def setUp(self):
        self.rows = [(date(2024, 1, 1) + timedelta(days=i), 100 + i)
                     for i in range(30)]

    def test_linear_trend(self):
        result = walk_forward(self.rows)
        self.assertEqual((result["train_count"], result["validation_count"],
                          result["test_count"]), (18, 6, 6))
        self.assertAlmostEqual(result["metrics"]["linear_regression"]["mae"], 0)
        self.assertEqual(result["metrics"]["persistence"]["mae"], 1)

    def test_test_values_cannot_select_window(self):
        before = walk_forward(self.rows)
        after = walk_forward(self.rows[:24] + [(d, 999) for d, _ in self.rows[24:]])
        self.assertEqual(before["window"], after["window"])
        self.assertEqual(before["validation_mae"], after["validation_mae"])
        for model in ("persistence", "moving_average", "linear_regression"):
            self.assertEqual(before["predictions"][0][model],
                             after["predictions"][0][model])

    def test_invalid_inputs(self):
        for rows in (self.rows[:10], list(reversed(self.rows)),
                     self.rows[:-1] + [(self.rows[-1][0], float("nan"))]):
            with self.assertRaises(ValueError):
                walk_forward(rows)
        with self.assertRaises(ValueError):
            walk_forward(self.rows, windows=(1,))
