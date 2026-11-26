import unittest
from app import app

class DashboardTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_dashboard(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Synthetic demo data", response.data)
        self.assertIn(b"Forecast errors", response.data)
        self.assertIn(b"moving_average", response.data)

    def test_window_selection(self):
        response = self.client.get("/?window=5")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'value="5" selected', response.data)

    def test_invalid_window(self):
        for value in ("bad", "0", "100"):
            response = self.client.get("/?window=" + value)
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'role="alert"', response.data)
