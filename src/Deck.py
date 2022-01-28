from random import randint

from Card import *


class Deck(list[Card]):
    def __init__(self):
        super().__init__()
        for face in Face:
            for suit in Suit:
                self.append(Card(face, suit))

    def shuffle(self):
        for i in range(52):
            random1 = randint(0, 51)
            random2 = randint(0, 51)
            card1 = self[random1]
            card2 = self[random2]
            self[random2] = card1
            self[random1] = card2
        return self

    def __str__(self):
        string = '['
        for card in self:
            string += card.__str__() + ', '
        return string[0:len(string) - 2] + ']'
