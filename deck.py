"""Deck management for the card game.

This module defines Deck class, which creates new card deck,
shuffles deck, deal cards to each player, and reveals bonus suit.
"""

__author__ = "BR"

import random


class Deck:
    """Represents the card deck used in the game.

    A card deck consists of 60 cards. Each card has a number
    from 1 to 15 and one of four suits: spades, hearts, diamonds,
    or clubs.
    """

    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        """Create and return a complete deck of cards.

        :returns: A list of card tuples.
        :rtype: list
        """
        suits = ["spades", "hearts", "diamonds", "clubs"]
        deck = [(suit, number) for suit in suits for number in range(1, 16)]
        return deck

    def deck_shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self, num_players, num_rounds):
        """Deal cards to each player.
        
        In round n, each player receives n cards.

        :param num_players: The number of players in the game.
        :type num_players: int
        :param num_rounds: The current round number.
        :type num_rounds: int
        :returns: A list of hands, one hand for each player.
        :rtype: list
        """
        hands = [[] for _ in range(0, num_players)]
        for i in range(0, num_rounds):
            for j in range(0, num_players):
                hands[j].append(self.cards.pop(0))
        
        return hands

    def show_bonus(self):
        return self.cards.pop(0)[0]

