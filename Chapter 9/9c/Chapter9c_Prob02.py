import os
os.system('cls||clear')

#----CODE STARTS HERE------

class WordWizards:
    def __init__(self, player1, player2, prefix):
        self.player1 = player1
        self.player2 = player2
        self.prefix = prefix.lower()

    def player_points(self, player, opponent):
        player_words = player.words.difference(opponent.words)
        return sum([len(word) for word in player_words if word.startswith(self.prefix)])

    def winner(self):
        player1_score = self.player_points(self.player1, self.player2)
        player2_score = self.player_points(self.player2, self.player1)
        if player1_score > player2_score:
            return self.player1.name
        if player2_score > player1_score:
            return self.player2.name
        return "draw"

class Player:
    def __init__(self, name):
        self.name = name
        self.words = set()

    def add_word(self, word):
        self.words.add(word.lower())