import sys

from PyQt5 import uic
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QMainWindow

from SolitaireDeck import *


class SolitaireSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('solitaire.ui', self)

        piles = {self.card1: s_deck.pile1, self.card8: s_deck.pile2, self.card14: s_deck.pile3,
                 self.card19: s_deck.pile4, self.card23: s_deck.pile5, self.card26: s_deck.pile6,
                 self.card28: s_deck.pile7}
        for pile in piles:
            first_card = piles[pile].__getitem__(len(piles[pile]) - 1)
            pile.setPixmap(QPixmap(first_card.image_location()))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    deck = Deck().shuffle()
    s_deck = SolitaireDeck(deck)
    solitaire_solver = SolitaireSolver()
    sys.exit(app.exec_())
