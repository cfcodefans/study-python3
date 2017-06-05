import logging
import unittest
import traceback as tb

logging.basicConfig(format="%(asctime)s\t%(levelname)s\t%(message)s", level=logging.INFO)


class LoggingTests(unittest.TestCase):
    logging.info("LoggingTests:init")

    def test_info(self):
        logging.info("LoggingTests:test_info")
        logging.info(tb.format_stack()[-1])

    pass


if __name__ == '__main__':
    unittest.main()
