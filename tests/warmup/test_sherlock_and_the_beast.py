import unittest

from warmup.sherlock_and_the_beast import decent_number


class TestSherlockAndTheBeast(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(decent_number(1),  '-1')
        self.assertEqual(decent_number(3),  '555')
        self.assertEqual(decent_number(5),  '33333')
        self.assertEqual(decent_number(11), '55555533333')


if __name__ == '__main__':
    unittest.main()
