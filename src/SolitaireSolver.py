import sys

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

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
    def __init__(self):
        super().__init__()
        uic.loadUi('solitaire.ui', self)

        deck = Deck().shuffle()
        self.s_deck = SolitaireDeck(deck)

        self.setMaximumSize(self.size())
        self.setWindowIcon(QIcon('resources\\solitaire_icon.png'))
        self.setWindowTitle('Solitaire Solver')

        # Generates and replaces each QLabel in the 7 piles
        for i in range(28):
            qlabel_card = self.findChild(QLabel, 'card' + (i + 1).__str__())
            pile_index = find_pile_index(i)
            pile = self.s_deck.piles[pile_index].pop()
            card_image = CardImage(pile, self.cards, qlabel_card, self)
            if len(self.s_deck.piles[pile_index]) == 0:
                card_image.flip()

        # Generates and replaces the extra pile cards
        for i in range(3):
            extra_card = self.findChild(QLabel, 'extra_card' + abs(i - 3).__str__())
            extra_image = CardImage(self.s_deck.current_extra(), self.cards,
                                    extra_card, self)
            extra_image.flip()
            extra_image.raise_()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    solitaire_solver = SolitaireSolver()
    sys.exit(app.exec_())
