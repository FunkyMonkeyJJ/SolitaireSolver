import os

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class CardImage(QLabel):
    def __init__(self, card, parent, widget):
        super().__init__(parent)
        # True = Back showing
        self.flipped = True
        self.card = card
        self.setSizePolicy(widget.sizePolicy())
        self.setScaledContents(True)
        self.setMinimumSize(widget.minimumSize())
        self.setGeometry(widget.geometry())
        self.setPixmap(widget.pixmap())
        widget.setParent(None)

        self.moving = False
        self.position = (self.geometry().x(), self.geometry().y())

    def flip(self):
        if self.flipped:
            self.setPixmap(QPixmap(self.card.image_location()))
        else:
            path = os.getcwd() + "\\resources\\card_back.png"
            self.setPixmap(QPixmap(path))
        self.flipped = not self.flipped

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.flipped:
            self.moving = True

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.moving:
            self.move(ev.x(), ev.y())

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.moving = False
        self.move(self.position[0], self.position[1])
        # TODO: If left on something that is able to, auto position it.
        #  Else, drop it back at original position.
