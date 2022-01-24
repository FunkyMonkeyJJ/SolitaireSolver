from Deck import *
from Pile import *


class SolitaireDeck(Deck):
    def __init__(self, deck):
        super().__init__()
        # Fills up the piles in the solitaire layout
        self.pile1 = Pile([deck.pop()])
        self.pile2 = Pile([deck.pop()])
        self.pile3 = Pile([deck.pop()])
        self.pile4 = Pile([deck.pop()])
        self.pile5 = Pile([deck.pop()])
        self.pile6 = Pile([deck.pop()])
        self.pile7 = Pile([deck.pop()])

        self.pile2.append(deck.pop())
        self.pile3.append(deck.pop())
        self.pile4.append(deck.pop())
        self.pile5.append(deck.pop())
        self.pile6.append(deck.pop())
        self.pile7.append(deck.pop())

        self.pile3.append(deck.pop())
        self.pile4.append(deck.pop())
        self.pile5.append(deck.pop())
        self.pile6.append(deck.pop())
        self.pile7.append(deck.pop())

        self.pile4.append(deck.pop())
        self.pile5.append(deck.pop())
        self.pile6.append(deck.pop())
        self.pile7.append(deck.pop())

        self.pile5.append(deck.pop())
        self.pile6.append(deck.pop())
        self.pile7.append(deck.pop())

        self.pile6.append(deck.pop())
        self.pile7.append(deck.pop())

        self.pile7.append(deck.pop())

        # All extra cards are left in their own pile
        self.extra = Pile(deck, True)
        self.copy_extra = self.extra

        # Piles where the cards go when they are found
        self.spades = Pile([], False, True)
        self.hearts = Pile([], False, True)
        self.clubs = Pile([], False, True)
        self.diamonds = Pile([], False, True)

    def __str__(self):
        return self.pile1[0].__str__()
