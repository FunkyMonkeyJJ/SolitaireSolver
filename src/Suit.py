from enum import Enum


class Suit(Enum):
    SPADES = 'spades'
    HEARTS = 'hearts'
    CLUBS = 'clubs'
    DIAMONDS = 'diamonds'

    def __str__(self):
        return self.value
