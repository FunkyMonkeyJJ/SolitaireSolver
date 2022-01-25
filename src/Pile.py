from Card import *


class Pile(list[Card]):
    def __init__(self, deck, extra=False, face=False):
        super().__init__()
        for card in deck:
            self.append(card)
        self.extra = extra
        self.face = face

    def __str__(self):
        string = '['
        for card in self:
            string += card.__str__() + ', '
        return string[0:len(string) - 2] + ']'
