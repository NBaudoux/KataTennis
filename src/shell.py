from tennisGame import *
from lang import *

class ShellInterface:
    def __init__ (self):
        """
        Class constructor
        """
        self.game = TennisGame()
        self.lang = Lang().current

        print(self.lang["WELCOME"])
        while(not self.game.done):
            self.displayScore()
            self.askScore()

    def displayScore(self):
        """
        Displaying current score
        """
        score0 = self.game.getPoints(0)
        score1 = self.game.getPoints(1)
        print(self.lang["PLAYER"]+" 1 - "+self.lang["PLAYER"]+" 2")
        for i in range(2):
            print(score0[i]+" - "+score1[i])

    def askScore(self):
        """
        Asking who has scored
        """
        notCorrect = True
        while(notCorrect):
            player = input(self.lang["WHO"]+" ")
            if player in ["0","1"]:
                notCorrect = False
            else:
                print(self.lang["NOTCORR"])

        self.process(int(player))

    def process(self, player):
        """
        Processing score
        Args: (int) player - player identifier (0 or 1)
        """
        self.game.incr(player)
        if(self.game.gameWon(player)):
            print(self.lang["WINNER"]+" "+str(player))

if __name__ == "__main__":
    ShellInterface()
