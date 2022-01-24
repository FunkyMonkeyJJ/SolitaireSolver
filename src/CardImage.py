import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class CardImage:
    default_image = QPixmap(os.getcwd() + "\\resources\\card_back.png")

    def __init__(self, card, widget):
        self.card = card
        self.image = QLabel(widget)
        self.image.setGeometry(0, 0, 100, 150)
        self.image.setPixmap(QPixmap(os.getcwd() + card.__str__()))
        print(os.getcwd() + card.__str__())
        self.image.show()
        # 500 x 726 Pixels
