from elem import *

class ImgButton(Elem):
    def __init__(self, root, imgLink, cmd, times=1):
        """
        Constructor for add button
        """
        self.cmd=cmd
        self.logo=PhotoImage(file=imgLink).subsample(int(10*times),int(10*times))
        self.elem=Button(root, image=self.logo, command=cmd)
        if "logo/submit.png" == imgLink:
            self.elem.bind("<Return>", self.callCmd)

    def callCmd(self, event):
        """
        Handles event if button binded
        """
        self.cmd()
