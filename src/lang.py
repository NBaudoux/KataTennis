class Lang:
    def __init__(self):
        self.langList = {"en": self.en()}
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
            "LANGNOT": "This language is not available yet",
            "NOTCORR": "You have not entered a valid number. Enter 0 or 1.",
            "PLAYER" : "Player",
            "WELCOME": "Welcome to KataTennis",
            "WHO"    : "Which player has scored (Enter 0 or 1)",
            "WINNER" : "The winner is"
            }
        return lang
