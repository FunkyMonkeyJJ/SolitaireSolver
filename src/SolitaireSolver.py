import sys
import os

from PyQt5 import uic
from PyQt5.Qt import *
# from PyQt5.uic import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from CardImage import *
from SolitaireDeck import *
# from solitaire_ui import *


class SolitaireSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('solitaire.ui', self)

        self.first_pile.setAlignment(Qt.AlignTop)
        self.second_pile.setAlignment(Qt.AlignTop)
        self.third_pile.setAlignment(Qt.AlignTop)
        self.fourth_pile.setAlignment(Qt.AlignTop)
        self.fifth_pile.setAlignment(Qt.AlignTop)
        self.sixth_pile.setAlignment(Qt.AlignTop)


        self.show()

    # def run(self, cards):
    #     self.show()
    # app = QApplication(sys.argv)
    # widget = QMainWindow()
    # window = Ui_MainWindow().setupUi(widget)
    # widget.setGeometry(0, 0, 500, 500)
    # widget.setWindowTitle("Solitaire")

    # for card in cards:
    #     card_image = CardImage(card, widget)

    # widget.show()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    solitaire_solver = SolitaireSolver()
    deck = Deck().shuffle()
    s_deck = SolitaireDeck(deck)
    sys.exit(app.exec_())
    # solitaire_solver.run(s_deck)
