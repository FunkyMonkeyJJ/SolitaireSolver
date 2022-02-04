from Pile import *


class SolitaireDeck:
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
        self.extra = Pile(deck)
        # self.copy_extra = self.extra
        self.extra_iter = 0

        # Piles where the cards go when they are found
        self.spades = Pile([])
        self.hearts = Pile([])
        self.clubs = Pile([])
        self.diamonds = Pile([])

    def current_extra(self):
        return self.extra[self.extra_iter]

    def draw_extra(self):
        if self.extra_iter >= len(self.extra):
            self.extra_iter = 0
        next_card = self.extra[self.extra_iter]
        self.extra_iter += 1
        return next_card

    def reset_extra(self):
        self.extra_iter = 0

    def __str__(self):
        return super().__str__()
