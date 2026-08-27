import unittest

from app import app


class AppSmokeTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"DSA for senior engineers", response.data)


if __name__ == "__main__":
    unittest.main()
