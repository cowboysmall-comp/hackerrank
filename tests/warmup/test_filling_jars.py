import unittest

from warmup.filling_jars import filling_jars


class TestFillingJars(unittest.TestCase):

    def test_basic_cases(self):
        operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

        self.assertEqual(filling_jars(operations, 5), 160)


if __name__ == '__main__':
    unittest.main()
