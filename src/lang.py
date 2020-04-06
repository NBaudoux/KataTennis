"""
This class makes easy to add any additional language
"""

class Lang:
    def __init__(self):
        self.langList = {"en": self.en()} #Add reference to new languages here
        self.switch("en")

    def switch(self, newLang):
        """
        Switching Language
        """
        if(newLang not in self.langList):
            raise IndexError("This language is not available yet")
        self.current=self.langList[newLang]

    def en(self):
        """
        Set of english text
        """
        lang={
            "EXIT"   : "Press ENTER to exit",
            "KATATEN": "KataTennis",
            "NOTCORR": "You have not entered a valid number. Enter 0 or 1.",
            "PLAYER" : "Player",
            "SCORE"   : "Score",
            "WELCOME": "Welcome to KataTennis",
            "WHO"    : "Which player has scored (Enter 0 or 1)",
            "WINNER" : "The winner is",
            "WON"    : "WON"
            }
        return lang

    #Additional languages may be added here
