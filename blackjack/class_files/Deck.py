#!/usr/bin/env python3

import random
from python_course.blackjack.class_files.Card import Card

_ranks = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
_cards = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


def assemble_deck():
    deck = []
    for rank in _ranks:
        for card in _cards:
            deck.append(Card(rank, card))

    random.shuffle(deck)
    return deck


class Deck:
    def __init__(self):
        self.deck = assemble_deck()

    def shuffle(self, new=False):
        if new:
            self.deck = assemble_deck()
        random.shuffle(self.deck)
        return self.deck

    def draw(self, num_cards=1):
        card_draw = []
        for card in range(num_cards):
            card_draw.append(self.deck.pop(0))

        return card_draw
