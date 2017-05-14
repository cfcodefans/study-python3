import unittest
import requests
import logging

import LoggingTests

class HttpClientTests(unittest.TestCase):
    def test_http_get(self):
        req: requests.Request = requests.get(url="https://www.bing.com/")
        logging.info(str(req))
        logging.info(str())

    pass


if __name__ == '__main__':
    unittest.main()
