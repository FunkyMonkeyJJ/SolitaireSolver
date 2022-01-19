from Face import Face
from Suit import Suit


class Card:
    def __init__(self, face=Face.ACE, suit=Suit.SPADES):
        self.suit = suit
        self.face = face

    def __str__(self):
        return str.format("({0} of {1})".format(self.face, self.suit))
