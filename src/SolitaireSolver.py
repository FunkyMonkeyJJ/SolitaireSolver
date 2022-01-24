import os
import sys

from PyQt5 import uic
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QMainWindow

from SolitaireDeck import *


class SolitaireSolver(QMainWindow):
    def __init__(self, cards):
        super().__init__()
        uic.loadUi('solitaire.ui', self)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    deck = Deck().shuffle()
    s_deck = SolitaireDeck(deck)
    solitaire_solver = SolitaireSolver(s_deck)
    sys.exit(app.exec_())
