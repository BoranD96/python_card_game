"""Logic for a single trick in one round of the game.

This module manages all situations in one trick, 
including card play, winner determination and score calculation.
"""

__author__ = "BR"


import ui

class Trick:
    """Implements the logic of a trick within one round.

    A Trick stores playing order, bonus suit in current round,
    the cards played in this trick, and the scores gained in this trick.
    It also determines the winner of the trick.
    """

    def __init__(self, bonus_suit, order, round_num, trick_num):
        """Initialize a Trick object.

        :param bonus_suit: The bonus suit of current round.
        :type bonus_suit: str
        :param order: A list of player instances representing the playing
                      order in this trick.
        :type order: list
        :param round_num: The current round number.
        :type round_num: int
        :param trick_num: The current trick number within the round.
        :type trick_num: int
        """
        self.order = order
        self.bonus_suit = bonus_suit
        self.round_num = round_num
        self.trick_num = trick_num
        self.played_cards = {}  # Maps each player to the card played.
        self.score_dict = {}  # Stores each player's score gained.
        self.win = None

    def run(self):
        """Run the full process of one trick.

        This method lets each player play one card in the current order, stores
        the played cards, determines the winner and calculates the scores for
        this trick, and rotates the playing order for the next trick.
        """
        for player in self.order: 
            ui.trick_infobar(self.round_num, self.trick_num, self.bonus_suit,
                             player, self.played_cards)
            ui.trick_act(player, player.score_round)
            a = player.play_card(ui.trick_choose_card(len(player.hand)) - 1)
            self.played_cards[player] = a

        # Determine winner and scores.
        self.win = self.winning_determine()
        self.calculate_score()
        ui.trick_show_scores(self.trick_num, self.round_num, 
                             self.played_cards, self.win, self.score_dict)

        # Reset trick-specific data for the next trick.
        self.played_cards = {}
        self.score_dict = {}

        # Rotate the starting player.
        self.order.append(self.order.pop(0)) 



    def winning_determine(self):
        """Determine the winner of the current trick.

        The winner is the player who played the highest-numbered card.
        If multiple players played the same highest number, a card of the
        bonus suit takes priority. If there is still a tie, the first such
        card encountered in the playing order wins.

        :returns: The Player instance that wins the trick.
        :rtype: Player
        """
        win = max(self.played_cards.items(), 
                  key=lambda item: item[1][1] + 
                  (0.5 if item[1][0] == self.bonus_suit else 0))[0]
        return win


    def calculate_score(self):
        """Calculate each player's score in current trick.

        The winner of the trick gets 2 points.
        Every player who played card with bonus suit gets 1 point.
        If both conditions are satisfied, player can get 3 points in total.
        """
        for player in self.order:
            score = 0
            if player == self.win:
                score += 2
            if self.played_cards[player][0] == self.bonus_suit:
                score += 1
            self.score_dict[player] = score
            player.score_round += score

