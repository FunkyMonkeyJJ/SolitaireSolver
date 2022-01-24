import array
import sys

import PyQt5
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from CardImage import *
# from CardImage import CardImage
from SolitaireDeck import *


class SolitaireSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('solitaire.ui', self)

        piles = {self.card1: s_deck.pile1, self.card8: s_deck.pile2,
                 self.card14: s_deck.pile3, self.card19: s_deck.pile4,
                 self.card23: s_deck.pile5, self.card26: s_deck.pile6,
                 self.card28: s_deck.pile7, self.extra_card1: s_deck.extra}
        for pile in piles:
            first_card = piles[pile].__getitem__(len(piles[pile]) - 1)
            pile.setPixmap(QPixmap(first_card.image_location()))

        playing_field = []
        cards = self.playing_field.findChildren(PyQt5.QtWidgets.QLabel)
        for i in range(len(cards)):
            card_image = CardImage(s_deck[i], self.playing_field, cards[i])
            playing_field.append(card_image)
            for pile in piles:
                first_card = piles[pile].__getitem__(len(piles[pile]) - 1)
                if first_card.image_location() == card_image.card.image_location():
                    card_image.flip()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    deck = Deck().shuffle()
    s_deck = SolitaireDeck(deck)
    solitaire_solver = SolitaireSolver()
    sys.exit(app.exec_())
