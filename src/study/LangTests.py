import unittest


class LangTest(unittest.TestCase):
    egg_count = 0

    def test_default_value(self):
        def todo_list(new_task, base_list=["woke up"]):
            base_list.append(new_task)
            return base_list

        print(todo_list("what"))
        print(todo_list("the fuck"))

    def test_var_scope(self):
        # egg_count += 12
        self.egg_count += 12


if __name__ == '__main__':
    unittest.main
