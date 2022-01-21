import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class CardImage:
    def __init__(self, card, widget):
        self.card = card
        self.image = QLabel(widget)
        self.image.setGeometry(10, 10, 400, 100)
        self.image.setPixmap(QPixmap(os.getcwd() + card.__str__()))
        self.image.show()
        # 500 x 726 Pixels
