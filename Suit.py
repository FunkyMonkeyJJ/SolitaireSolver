from enum import Enum


class Suit(Enum):
    SPADES = 'Spades'
    HEARTS = 'Hearts'
    CLUBS = 'Clubs'
    DIAMONDS = 'Diamonds'

    def __str__(self):
        return self.value
