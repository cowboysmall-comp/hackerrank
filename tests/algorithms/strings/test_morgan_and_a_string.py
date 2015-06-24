import unittest

from algorithms.strings.morgan_and_a_string import merge


class TestMorganAndAString(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(merge('JACK', 'DANIEL'), 'DAJACKNIEL')
        self.assertEqual(merge('ABACABA', 'ABACABA'), 'AABABACABACABA')


if __name__ == '__main__':
    unittest.main()
