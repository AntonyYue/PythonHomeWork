# test_bowling.py

import unittest
from bowling import score_game

class TestBowlingScoring(unittest.TestCase):
    def test_all_strikes(self):

        self.assertEqual(score_game([10]*12), 300)

    def test_all_spares(self):

        self.assertEqual(score_game([5, 5]*10 + [5]), 150)

    def test_no_spares_no_strikes(self):

        self.assertEqual(score_game([3]*20), 60)

    def test_random_case_1(self):
        rolls = [10, 9, 1, 5, 5, 7, 2, 10, 10, 10, 9, 0, 8, 2, 9, 1, 10]
        self.assertEqual(score_game(rolls), 187)



if __name__ == '__main__':
    unittest.main()
