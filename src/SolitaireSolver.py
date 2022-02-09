import sys

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from Deck import *
from SolitaireDeck import *
from Stack import *


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

        # Generates and replaces each QLabel in the extra pile
        self.draw_pile = Stack()
        for i in range(24):
            qlabel_card = self.findChild(
                QLabel, 'extra_card' + (i + 1).__str__())
            extra_card = self.s_deck.draw_extra()
            card_image = CardImage(extra_card, self.cards, qlabel_card, self)
            self.draw_pile.append(card_image)
        print(self.draw_pile)

        self.extra_cards_button.clicked.connect(self.reset_extra_cards)

        self.show()

    def reset_extra_cards(self):
        self.draw_pile.reset()
        temp_tail = self.draw_pile.tail
        while temp_tail is not None:
            card = temp_tail.value
            card.move(20, 20)
            card.flip()
            temp_tail = temp_tail.next


if __name__ == '__main__':
    app = QApplication(sys.argv)
    SolitaireSolver()
    sys.exit(app.exec_())
