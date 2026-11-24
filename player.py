"""Player management for the card game.

This module defines the Player class, which stores player information,
hand cards, and score values.
"""

__author__ = "BR"


class Player:
    """Represents a player in the game.
     
    A player stores their name, current hand, score in the current round,
    and total score in the whole game.
    """

    def __init__(self, name):
        """Initialize a Player object.

        :param name: The player's name.
        :type name: str
        """
        self.name = name
        self.order = 0
        self.hand = []
        self.score_round = 0
        self.score_total = 0

    def play_card(self, played_index=0):
        """Play and return a card from the player's hand.

        :param played_index: The index of the card to play.
        :type played_index: int
        :returns: The selected card.
        :rtype: tuple
        """
        return self.hand.pop(played_index)

