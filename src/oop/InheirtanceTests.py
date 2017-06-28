import logging
import unittest

logging.basicConfig(format="%(asctime)s\t%(levelname)s\t%(message)s", level=logging.INFO)


class Base(object):
    def __init__(self):
        logging.info("Base")


class Foo(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
        logging.info("Foo")

if __name__ == '__main__':
    foo: Foo = Foo()
