"""
'Back-end', handling scores and its representations using:
* amount of points (0, 15, 30, 40, AD)
* names of score   (love, fifteen, thirty, forty, deuce, advantage)
"""

#   --- Imports ---
from consts import * #Containing points and names

class TennisGame:
    def __init__(self):
        """
        Class constructor
        """
        self.score = [0,0]
        self.done  = False

    def reset(self):
        """
        Resets scores
        """
        self.score = [0,0]
        self.done  = False

    def incr(self, player):
        """
        Incrementing a player's score
        Args: (int) player - player identifier (0 or 1)
        """
        if (player not in [0,1]):
            raise IndexError("Not in range")
        elif (not self.done):
            self.score[player] += 1
            self.gameWon(player)
        else:
            raise RuntimeError("Game is done")

    def getPoints(self, player):
        """
        Get a player's score in terms of points
        Args:    (int) player      - player identifier (0 or 1)
        Returns: (str, str) res    - points (0, 15, 30, 40, AD)
                                   - name   (love, fifteen, thirty, forty,
                                             deuce, advantage)
        """
        if (player not in [0,1]):
            raise IndexError("Not in range")
        res = ("", "")
        localScore = self.score[player]
        otherScore = self.score[player-1] #Score of the other player
        if (localScore < 3 or otherScore < 3):
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
                self.done = True
        return res
