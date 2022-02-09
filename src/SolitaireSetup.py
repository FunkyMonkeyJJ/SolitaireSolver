import sys

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from Deck import *
from Stack import *


# Returns the pile number for the given card number
def find_pile_index(card_num):
    if 6 >= card_num >= 0:
        return card_num
    piles = {7: 2, 8: 3, 9: 4, 14: 4, 10: 5, 15: 5, 19: 5, 11: 6,
             16: 6, 20: 6, 23: 6, 12: 7, 17: 7, 21: 7, 24: 7,
             26: 7, 13: 3, 18: 4, 22: 5, 25: 6, 27: 7}
    return piles.get(card_num) - 1


class SolitaireSetup(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('solitaire.ui', self)

        self.setMaximumSize(self.size())
        self.setWindowIcon(QIcon('resources\\solitaire_icon.png'))
        self.setWindowTitle('Solitaire Solver')

        deck = Deck().shuffle()

        # Creates each of the 7 Stacks for the playing field
        self.stacks = []
        for i in range(7):
            self.stacks.append(Stack())

        # Generates and replaces each QLabel in the 7 playing field Stacks
        for i in range(28):
            qlabel_card = self.findChild(QLabel, 'card' + (i + 1).__str__())
            card_image = CardImage(deck.pop(), self.cards, qlabel_card, self)

            pile_index = find_pile_index(i)
            self.stacks[pile_index].append(card_image)
            if len(self.stacks[pile_index]) == pile_index + 1:
                card_image.flip()

        # Generates and replaces each QLabel in the draw pile Stack
        self.draw_pile = Stack()
        for i in range(24):
            draw_card_str = 'draw_card' + (i + 1).__str__()
            qlabel_card = self.findChild(QLabel, draw_card_str)
            card_image = CardImage(deck.pop(), self.cards, qlabel_card, self)
            self.draw_pile.append(card_image)

        self.draw_cards_button.clicked.connect(self.reset_extra_cards)

        # Stacks where the cards go when they are found
        self.spades = Stack()
        self.hearts = Stack()
        self.clubs = Stack()
        self.diamonds = Stack()

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
    SolitaireSetup()
    sys.exit(app.exec_())
