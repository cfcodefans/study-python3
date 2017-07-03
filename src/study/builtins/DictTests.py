import unittest


class DictTests(unittest.TestCase):
    def test_create_map(self):
        _map: dict = {'a': 1}
        print(_map['a'])

    def test_keys(self):
        _map: dict = {'a': 1}
        for k in _map.keys():
            print(k)

if __name__ == '__main__':
    unittest.main
