import os

from Face import Face
from Suit import Suit


class Card:
    def __init__(self, face=Face.ACE, suit=Suit.SPADES):
        self.suit = suit
        self.face = face

    def image_location(self):
        return str.format("{0}\\resources\\{1}".format(os.getcwd(), self.__str__()))

    def __str__(self):
        return str.format("{0}_of_{1}.png".format(self.face.value, self.suit))
