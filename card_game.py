"""Main script for running card game.

This module starts the game, creates player instances, goes through all rounds,
shows the final game summary, and handles restarting or quitting the game.
"""

__author__ = 'BR'

import ui
from player import Player
from round import Round


def main():
    """
    Control the game loop until the players choose to end the game.
    """
    while True:
        # Game set up.
        player_names = ui.game_players()
        player_list = [Player(name) for name in player_names]
        rounds = 1
        # rounds = (60 - 1) // len(player_list)

        # Run the game process and determine winner.
        for round_num in range(1, rounds + 1):
            current_round = Round(player_list, round_num)
            current_round.run()
        winner = max(player_list, key=lambda player: player.score_total)
        ui.game_summary(player_list, winner)

        # Choose restart or quit.
        choice = ui.game_restart()
        if choice == 'r':
            continue
        else:
            break


if __name__ == '__main__':
    main()