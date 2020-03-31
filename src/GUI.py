#   --- Imports ---
from tennisGame import *
from lang import *

from tkinter import *
from tkinter.messagebox import showinfo

#   --- Local constants ---
FONT = ('Arial', 20)

#   --- GUI Class ---
class GUI:
    def __init__(self):
        """
        GUI class constructor
        """
        self.lang = Lang().current
        self.game = TennisGame()
        #GUI initialisation
        self.root=Tk(self.lang["KATATEN"])
        self.root.title("")
        self.root.minsize(200,200)

        self.displayTopFrame()

    def displayTopFrame(self):
        """
        Display top frame
        """
        self.topFrame = Frame(self.root)
        self.topFrame.grid(row=0, sticky=N+S+W+E)

        self.frames = []
        self.labels = []
        self.labelPoints = []
        self.labelNames  = []
        self.incrButtons = []
        for i in range(2):
            self.frames.append(Frame(self.topFrame))
            self.frames[i].grid(row=0,column=i)
            score = self.game.getPoints(i)
            self.labels.append(Label(self.frames[i], text=self.lang["PLAYER"]+" "+str(i), font=FONT))
            self.labels[i].grid(row=0)
            self.labelPoints.append(Label(self.frames[i], text=str(score[0]), font=FONT))
            self.labelPoints[i].grid(row=1)
            self.labelNames.append(Label(self.frames[i], text=str(score[1]), font=FONT))
            self.labelNames[i].grid(row=2)
        #Score button
        self.logo=PhotoImage(file="logo/add.png").subsample(15,15)
        self.incrButtons.append(Button(self.frames[0], image=self.logo, command=lambda: self.process(0)))
        self.incrButtons[0].grid(row=3)
        self.incrButtons.append(Button(self.frames[1], image=self.logo, command=lambda: self.process(1)))
        self.incrButtons[1].grid(row=3)

    def update(self):
        """
        Update information displayed
        """
        for i in range(2):
            score = self.game.getPoints(i)
            self.labelPoints[i].config(text=str(score[0]))
            self.labelNames[i].config(text=str(score[1]))

    def process(self, player):
        """
        Processing score
        Args: (int) player - player identifier (0 or 1)
        """
        self.game.incr(player)
        if(self.game.done):
            finalText = self.lang["WINNER"]+" "
            finalText += self.lang["PLAYER"]+" "
            finalText += str(player)
            showinfo(self.lang["WON"],finalText)
            self.topFrame.destroy()
            self.game.reset()
            self.displayTopFrame()
        else:
            self.update()

if __name__ == "__main__":
    main=GUI()
    main.root.mainloop()
