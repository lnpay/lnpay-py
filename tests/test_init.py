import unittest
import lnpay_py


class TestInit(unittest.TestCase):
    def test_initialization(self):
        key = "123"
        default_wak = "345"
        endpoint = "https://google.com"
        params = {
            "endpoint_url": endpoint
        }

        lnpay_py.initialize(key, default_wak, params)

        self.assertEqual(key, lnpay_py.__PUBLIC_API_KEY__)
        self.assertEqual(default_wak, lnpay_py.__DEFAULT_WAK__)
        self.assertEqual(endpoint, lnpay_py.__ENDPOINT_URL__)


if __name__ == '__main__':
    unittest.main()
