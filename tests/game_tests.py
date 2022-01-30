import unittest
from modules.game import Game, display_winner
from modules.player import Player

class TestGame(unittest.TestCase):

    def test_player_1_wins_with_rock(self):
        player_1 = Player("Player_1", "rock")
        player_2 = Player("Player_2", "scissors")
        result = Game.get_winner(self, player_1, player_2)
        self.assertEqual(player_1, result)

    def test_player_1_wins_with_scissors(self):
        player_1 = Player("Player_1", "scissors")
        player_2 = Player("Player_2", "paper")
        result = Game.get_winner(self, player_1, player_2)
        self.assertEqual(player_1, result)

    def test_player_1_wins_with_paper(self):
        player_1 = Player("Player_1", "paper")
        player_2 = Player("Player_2", "rock")
        result = Game.get_winner(self, player_1, player_2)
        self.assertEqual(player_1, result)

    def test_player_2_wins_with_rock(self):
        player_1 = Player("Player_1", "scissors")
        player_2 = Player("Player_2", "rock")
        result = Game.get_winner(self, player_1, player_2)
        self.assertEqual(player_2, result)

    def test_player_2_wins_with_scissors(self):
        player_1 = Player("Player_1", "paper")
        player_2 = Player("Player_2", "scissors")
        result = Game.get_winner(self, player_1, player_2)
        self.assertEqual(player_2, result)

    def test_player_2_wins_with_paper(self):
        player_1 = Player("Player_1", "rock")
        player_2 = Player("Player_2", "paper")
        result = Game.get_winner(self, player_1, player_2)
        self.assertEqual(player_2, result)

    def test_draw_gets_none(self):
        player_1 = Player("Player_1", "rock")
        player_2 = Player("Player_2", "rock")
        result = Game.get_winner(self, player_1, player_2)
        self.assertEqual(None, result)