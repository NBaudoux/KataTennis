import unittest
import sys
import os

#importing code to test
source = os.path.dirname(__file__) + "\..\src"
sys.path.append(source)
from tennisGame import *

game = TennisGame()

class TestTennisGame(unittest.TestCase):

    def test_reset(self):
        game.score[0] = 4
        game.score[1] = 3
        self.assertEqual(game.score[0], 4)
        self.assertEqual(game.score[1], 3)

        game.reset()
        self.assertEqual(game.score[0], 0)
        self.assertEqual(game.score[1], 0)

    def test_incr(self):
        game.reset()
        game.incr(0)
        self.assertEqual(game.score[0], 1)
        self.assertEqual(game.score[1], 0)

        #Testing IndexError
        with self.assertRaises(IndexError):
            game.getPoints(3)

    def test_getPoints(self):
        #Testing scores from 0 to 30 for both players
        game.reset()
        for i in range(3):
            self.assertEqual(game.getPoints(0), (POINTS[i], NAMES[i]) )
            self.assertEqual(game.getPoints(1), (POINTS[i], NAMES[i]) )
            game.incr(0)
            game.incr(1)

        #Testing scores from 0 to 40 for only one player
        game.reset()
        for i in range(4):
            self.assertEqual(game.getPoints(0), (POINTS[i], NAMES[i]) )
            self.assertEqual(game.getPoints(1), (POINTS[0], NAMES[0]) )
            game.incr(0)

        #Testing score 40
        game.reset()
        game.score[0] = 3
        self.assertEqual(game.getPoints(0), (POINTS[3], NAMES[3]) )

        #Testing deuce
        game.reset()
        game.score[0] = 3
        game.score[1] = 3
        self.assertEqual(game.getPoints(0), (POINTS[DEUCE], NAMES[DEUCE]) )
        self.assertEqual(game.getPoints(1), (POINTS[DEUCE], NAMES[DEUCE]) )

        game.reset()
        game.score[0] = 5
        game.score[1] = 5
        self.assertEqual(game.getPoints(0), (POINTS[DEUCE], NAMES[DEUCE]) )
        self.assertEqual(game.getPoints(1), (POINTS[DEUCE], NAMES[DEUCE]) )

        #Testing advantage
        game.reset()
        game.score[0] = 5
        game.score[1] = 6
        self.assertEqual(game.getPoints(0), (POINTS[NOTADV], NAMES[NOTADV]) )
        self.assertEqual(game.getPoints(1), (POINTS[ADV], NAMES[ADV]) )

        #Testing IndexError
        with self.assertRaises(IndexError):
            game.getPoints(2)

    def test_gameWon(self):
        game.reset()
        for i in range(4):
            self.assertFalse(game.gameWon(0))
            self.assertFalse(game.gameWon(1))
            game.incr(0) #Player 0 scoring
        self.assertTrue(game.gameWon(0))
        self.assertFalse(game.gameWon(1))

        #Testing with deuce/advantage
        game.reset()
        for i in range(5):
            self.assertFalse(game.gameWon(0))
            self.assertFalse(game.gameWon(1))
            game.incr(0) #Player 0 scoring
            game.incr(1) #Player 1 scoring
        self.assertFalse(game.gameWon(0))
        self.assertFalse(game.gameWon(1))
        game.incr(0) #Player 0 scoring
        self.assertFalse(game.gameWon(0))
        self.assertFalse(game.gameWon(1))
        game.incr(0) #Player 0 scoring
        self.assertTrue(game.gameWon(0))
        self.assertFalse(game.gameWon(1))

if __name__ == '__main__':
    unittest.main()
