import os

from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


# Replaces the current QLabel on the GUI, links information
# to the new QLabel, and creates custom events
class CardImage(QLabel):
    moving_memory = 0

    def __init__(self, card, parent, widget):
        super().__init__(parent)
        # True = Back showing; False = Face showing
        self.flipped = True
        self.card = card
        self.moving = False

        self.setSizePolicy(widget.sizePolicy())
        self.setScaledContents(True)
        self.setMinimumSize(widget.minimumSize())
        self.setPixmap(widget.pixmap())
        self.setGeometry(widget.geometry())
        self.position = (self.geometry().x(), self.geometry().y())

        # Deletes the base widget from the GUI
        widget.setParent(None)

    # Changes image of card to front/back respectively
    # Cards with the back facing cannot be moved
    def flip(self):
        if self.flipped:
            self.setPixmap(QPixmap(self.card.image_location()))
        else:
            path = os.getcwd() + "\\resources\\card_back.png"
            self.setPixmap(QPixmap(path))
        self.flipped = not self.flipped

    # Covered by another card; cannot be moved
    def is_covered(self):
        for child in self.parent().findChildren(QLabel):
            pos1 = self.pos()
            pos2 = child.pos()
            # In same pile and on top of pile
            if abs(pos1.x() - pos2.x()) == 0 and pos2.y() > pos1.y():
                return True
        return False

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if not self.flipped and not self.is_covered():
            self.moving = True

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.moving:
            # Moves the center of the card to the mouse
            self.move(self.mapToParent(ev.pos().__add__(QPoint(-50, -75))))

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.moving = False
        self.move(self.position[0], self.position[1])
        # TODO: If left on something that is able to, auto position it.
        #  Else, drop it back at original position.
