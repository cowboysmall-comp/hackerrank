import unittest

from algorithms.implementation.acm_icpc_team import max_topics


class TestACMICPCTeam(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(max_topics([21, 28, 26, 5]), (5, 2))


if __name__ == '__main__':
    unittest.main()
