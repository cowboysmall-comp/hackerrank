import unittest

from warmup.sherlock_and_gcd import powerset, gcd, gcd_multiple, check_condition


class TestSherlockAndGCD(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(check_condition([1, 2, 3]), 'YES')
        self.assertEqual(check_condition([2, 4]), 'NO')
        self.assertEqual(check_condition([5, 5, 5]), 'NO')


    def test_gcd(self):
        self.assertEqual(gcd(2, 3), 1)
        self.assertEqual(gcd(2, 4), 2)


    def test_gcd_multiple(self):
        self.assertEqual(gcd_multiple([2, 3, 5, 7]), 1)
        self.assertEqual(gcd_multiple([3, 6, 9]), 3)


    def test_powerset(self):
        s1 = sorted(list(powerset(set([1, 2, 3]))), key = lambda x: sum(x))
        s2 = [set(), set([1]), set([2]), set([3]), set([1, 2]), set([1, 3]), set([2, 3]), set([1, 2, 3])]
        self.assertEqual(s1, s2)


if __name__ == '__main__':
    unittest.main()
