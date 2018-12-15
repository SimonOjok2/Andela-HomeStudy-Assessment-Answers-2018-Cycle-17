import unittest

from number_game import number_game


class Tests(unittest.TestCase):
    def test_function(self):
        self.assertEqual(number_game(2,12), [3, 5, 7, 9, 11])
        self.assertEqual(number_game(0,0), [])
        self.assertEqual(number_game(2,12), [3, 5, 7, 9, 11])
        self.assertEqual(number_game(200,180), [180, 182, 184, 186, 188, 190, 192, 194, 196, 198])
        self.assertEqual(number_game(180,200), [181, 183, 185, 187, 189, 191, 193, 195, 197, 199])
