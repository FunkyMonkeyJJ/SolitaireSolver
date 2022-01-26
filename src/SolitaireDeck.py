from Deck import *
from Pile import *


class SolitaireDeck(Deck):
    def __init__(self, deck):
        super().__init__()

        # Creates each of the 7 piles for the playing field
        self.piles = []
        for i in range(7):
            self.piles.append(Pile([]))

        # Fills up the piles in the solitaire layout
        j = 0
        min_index = 0
        for i in range(28):
            self.piles[j].append(deck.pop())
            if len(self.piles[j]) - 1 == j:
                min_index = j
            if j == 6:
                j = min_index
            j += 1

        # All extra cards are left in their own pile
        self.extra = Pile(deck, True)
        self.copy_extra = self.extra
        self.current_extra = 1

        # Piles where the cards go when they are found
        self.spades = Pile([], False, True)
        self.hearts = Pile([], False, True)
        self.clubs = Pile([], False, True)
        self.diamonds = Pile([], False, True)

    def current_extra(self):
        self.current_extra += 1
        if self.current_extra > len(self.extra):
            self.current_extra = 0
        return self.current_extra

    def __str__(self):
        return self.piles[0].__str__()
