import unittest

from algorithms.implementation.angry_professor import angry_professor


class TestAngryProfessor(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(angry_professor(3, [-1, -3, 4, 2]), 'YES')
        self.assertEqual(angry_professor(2, [0, -1, 2, 1]), 'NO')


if __name__ == '__main__':
    unittest.main()
