from flask import render_template, request, redirect
from app import app
from modules.game import Game
from modules.player import Player


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/<choice_1>/<choice_2>')
def display_winner(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    play_game = Game(player_1, player_2)
    winner = Game.get_winner(play_game)
    return render_template('index.html', player_1=player_1, player_2=player_2, winner=winner)

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/game')
def game_page():
    return render_template('game.html')

@app.route('/game', methods=['POST'])
def game():
    name = request.form["name"]
    player_choice = request.form["options"]
    player_1 = Player(name, player_choice)
    player_2 = Game.computer()
    play_game = Game(player_1, player_2)
    winner = Game.get_winner(play_game)
    return render_template('index.html', player_1=player_1, player_2=player_2, winner=winner)