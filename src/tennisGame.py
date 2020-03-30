#   --- Imports ---
from consts import *

class TennisGame:
    def __init__(self):
        """
        Class constructor
        """
        self.score = [0,0]

    def reset(self):
        """
        Resets scores
        """
        self.score = [0,0]

    def incr(self, player):
        """
        Incrementing a player's score
        Args: (int) player - player identifier (0 or 1)
        """
        if (player not in [0,1]):
            raise IndexError("Not in range")
        self.score[player] += 1

    def getPoints(self, player):
        """
        Get a player's score in terms of points
        Args:    (int) player - player identifier (0 or 1)
        Returns: (str) res    - points (0, 15, 30, 40, AD)
        """
        if (player not in [0,1]):
            raise IndexError("Not in range")
        res = ("", "")
        localScore = self.score[player]
        otherScore = self.score[player-1] #Score of the other player
        if (localScore <= 3 and otherScore < 3):
            res = (POINTS[localScore], NAMES[localScore])
        else:
            if(otherScore < localScore):
                res = (POINTS[ADV], NAMES[ADV])
            elif(otherScore > localScore):
                res = (POINTS[NOTADV], NAMES[NOTADV])
            else:
                res = (POINTS[DEUCE], NAMES[DEUCE])
        return res

    def gameWon(self, player):
        """
        Determine if a game is won and update
        Args:    (int)  player - player identifier (0 or 1)
        Returns: (bool) res    - True if won by player given in arg;
                                 False otherwise.
        """
        if (player not in [0,1]):
            raise IndexError("Not in range")
        res = False
        localScore = self.score[player]
        if(localScore > 3):
            otherScore = self.score[player-1]
            diff = localScore - otherScore;
            if(diff >= 2):
                res = True
        return res
