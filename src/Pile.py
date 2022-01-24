from Card import *


class Pile(list[Card]):
    def __init__(self, deck, extra=False, face=False):
        super().__init__()
        for card in deck:
            self.append(card)
        self.extra = extra
        self.face = face

    # def __str__(self):
    #     if self.extra:
    #         print('Only three cards, with one showing on top.')
    #     elif self.face:
    #         print('Only show the top card.')
    #     else:
    #         print('As many cards as in the pile, with one showing on top.')
