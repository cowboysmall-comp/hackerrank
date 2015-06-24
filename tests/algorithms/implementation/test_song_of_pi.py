import unittest

from algorithms.implementation.song_of_pi import pi_song


class TestSongOfPi(unittest.TestCase):

    def test_basic_cases(self):
        PI = [int(c) for c in '31415926535897932384626433833']

        self.assertEqual(pi_song('Can I have a large container of coffee right now', PI), 'It\'s a pi song.')
        self.assertEqual(pi_song('Can I have a large container of tea right now', PI), 'It\'s not a pi song.')
        self.assertEqual(pi_song('Now I wish I could recollect pi Eureka cried the great inventor Christmas Pudding Christmas Pie Is the problems very center', PI), 'It\'s a pi song.')


if __name__ == '__main__':
    unittest.main()
