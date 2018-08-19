import unittest


class DictTests(unittest.TestCase):
    def test_create_map(self):
        _map: dict = {'a': 1}
        print(_map['a'])

    def test_keys(self):
        _map: dict = {'a': 1}
        for k in _map.keys():
            print(k)

    def test_items(self):
        _map: dict = {'a': 1}
        for e in _map.items():
            print(e)

    def test_put(self):
        _map: dict = {}
        _map['a'] = 1
        print(_map)

    def test_max(self):
        _map: dict = dict([(i, 10 - i) for i in range(10)])
        print(_map)
        _map[1] = 10
        print(max(_map.items(), key=lambda item: item[1]))

    def test_reverse(self):
        def most_prolific(_dict):
            year_nums = dict([(v, 0) for v in _dict.values()])
            for _item in _dict.items():
                year_nums[_item[1]] += 1

            num_years = dict([(v, []) for v in year_nums.values()])
            for _item in year_nums.items():
                num_years[_item[1]] += [_item[0]]

            max_num_years = max(num_years.items())[1]
            if len(max_num_years) == 1:
                return max_num_years[0]
            else:
                return max_num_years

        beatles_discography: dict[str, str] = {"Please Please Me": 1963, "With the Beatles": 1963,
                                               "A Hard Day's Night": 1964, "Beatles for Sale": 1964,
                                               "Twist and Shout": 1964,
                                               "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
                                               "Sgt. Pepper's Lonely Hearts Club Band": 1967,
                                               "Magical Mystery Tour": 1967, "The Beatles": 1968,
                                               "Yellow Submarine": 1969, 'Abbey Road': 1969,
                                               "Let It Be": 1970}

        print(most_prolific(beatles_discography))


if __name__ == '__main__':
    unittest.main
