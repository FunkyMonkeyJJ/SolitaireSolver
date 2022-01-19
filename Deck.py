from random import randint

from Face import Face
from Suit import Suit
from Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for face in Face:
            for suit in Suit:
                self.cards.append(Card(face, suit))

    def shuffle(self):
        for i in range(52):
            random1 = randint(0, 51)
            random2 = randint(0, 51)
            card1 = self.cards[random1]
            card2 = self.cards[random2]
            self.cards[random2] = card1
            self.cards[random1] = card2
        return self

    def __str__(self):
        string = '['
        for card in self.cards:
            string += card.__str__() + ', '
        return string[0:len(string) - 2] + ']'
