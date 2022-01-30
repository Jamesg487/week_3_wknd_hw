import random
from modules.player import Player


class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def get_winner(self):
        if self.player_1.choice == "rock" and self.player_2.choice == "scissors":
            return self.player_1
        if self.player_1.choice == "scissors" and self.player_2.choice == "paper":
            return self.player_1
        if self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return self.player_1
        if self.player_1.choice == "scissors" and self.player_2.choice == "rock":
            return self.player_2
        if self.player_1.choice == "paper" and self.player_2.choice == "scissors":
            return self.player_2
        if self.player_1.choice == "rock" and self.player_2.choice == "paper":
            return self.player_2
        if self.player_1.choice == self.player_2.choice:
            return None

    def computer():
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        computer = Player("Computer", computer_choice)
        return computer

     