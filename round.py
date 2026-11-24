"""Logic for a single round in one game.

This module manage all situations in one round, including determining
player order, card dealing, bonus suit setup, trick execution, and round
score updates.
"""

__author__ = 'BR'

import random

from deck import Deck
from trick import Trick
import ui


class Round:
    """Implements the logic of a round within one game.

    A Round stores the playing order, the deck used in this round, the
    bonus suit, and the current round number.
    It also updates round results in player scores.
    """

    def __init__(self, player_list, round_num):
        """Initialize a Round object.

        :param player_list: A list of Player instances in the game.
        :type player_list: list
        :param round_num: The current round number.
        :type round_num: int
        """
        self.player_list = player_list
        self.round_num = round_num
        self.order = random.sample(self.player_list, len(player_list))
        self.deck = Deck()
        self.bonus_suit = None
        self.trick_num = 0

    def run(self):
        """Run the full process of one round.

        This method shows round information, deals cards to each player,
        determines the bonus suit, run tricks until all cards are played,
        updates total scores, shows round summary, and resets round scores for
        each player.
        """
        self.order_name = [player.name for player in self.order]
        ui.round_infobar(self.round_num, self.order_name)

        self.deck.deck_shuffle()
        hands = self.deck.deal_cards(len(self.order), self.round_num)
        for i in range(len(self.order)):
            self.order[i].hand.extend(hands[i])

        self.bonus_suit = self.deck.show_bonus()

        ui.round_bonus(self.bonus_suit)

        while True:
            if self.is_finished():
                break
            self.trick_num += 1
            trick = Trick(
                self.bonus_suit,
                self.order,
                self.round_num,
                self.trick_num
            )
            trick.run()

        self.score_update()
        
        ui.round_show_scores(self.round_num, self.player_list)

        for player in self.order:
            player.score_round = 0

    def score_update(self):
        """Add each player's round score to their total score."""
        for player in self.order:
            player.score_total += player.score_round

    def is_finished(self):
        """Check whether the current round has finished.

        A round is finished when the first player in the current order has no
        cards left in hand. Since all players receive and play the same number
        of cards, this is enough to determine whether the round is over.

        :returns: True if all cards in this round have been played.
        :rtype: bool
        """
        return self.order[0].hand == []
    
