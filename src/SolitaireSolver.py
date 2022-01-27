import sys

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from CardImage import *
from Deck import *
from SolitaireDeck import *


# Returns the pile number for the given card number
def find_pile_index(card_num):
    if 6 >= card_num >= 0:
        return card_num
    piles = {7: 2, 8: 3, 9: 4, 14: 4, 10: 5, 15: 5, 19: 5, 11: 6,
             16: 6, 20: 6, 23: 6, 12: 7, 17: 7, 21: 7, 24: 7,
             26: 7, 13: 3, 18: 4, 22: 5, 25: 6, 27: 7}
    return piles.get(card_num) - 1


class SolitaireSolver(QMainWindow):
    deck = Deck().shuffle()
    s_deck = SolitaireDeck(deck)

    def __init__(self):
        super().__init__()
        uic.loadUi('solitaire.ui', self)

        self.setMaximumSize(self.size())
        self.setWindowIcon(QIcon('resources\\solitaire_icon.png'))
        self.setWindowTitle('Solitaire Solver')

        for i in range(28):
            qlabel_card = self.findChild(QLabel, 'card' + (i + 1).__str__())
            pile_index = find_pile_index(i)
            pile = self.s_deck.piles[pile_index].pop()
            card_image = CardImage(pile, self.cards, qlabel_card)
            if len(self.s_deck.piles[pile_index]) == 0:
                card_image.flip()

        extra_card1 = self.findChild(QLabel, 'extra_card1')
        extra_image1 = CardImage(self.s_deck.current_extra(), self.cards, extra_card1)
        extra_image1.flip()
        extra_card2 = self.findChild(QLabel, 'extra_card2')
        extra_image2 = CardImage(self.s_deck.current_extra(), self.cards, extra_card2)
        extra_image2.flip()
        extra_card3 = self.findChild(QLabel, 'extra_card3')
        extra_image3 = CardImage(self.s_deck.current_extra(), self.cards, extra_card3)
        extra_image3.flip()
        extra_image2.raise_()
        extra_image1.raise_()

        # TODO: Somewhere between line 49 and line 56, there is a change
        #  in the location in memory of the SolitaireSolver.s_deck, which
        #  leads to there being a completely different shuffled deck being
        #  called in the three places after line 49.

        print(self.s_deck)
        print(SolitaireSolver.s_deck)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    solitaire_solver = SolitaireSolver()
    print(SolitaireSolver.s_deck.extra)
    sys.exit(app.exec_())
