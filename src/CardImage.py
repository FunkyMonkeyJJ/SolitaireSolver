import os

from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

import SolitaireSolver
from Face import *


# Replaces the current QLabel on the GUI, links information
# to the new QLabel, and creates custom events
class CardImage(QLabel):
    def __init__(self, card, parent, widget):
        super().__init__(parent)
        # True = Back showing; False = Face showing
        self.is_flipped = True
        self.is_moving = False
        self.card = card
        self.cards_below = []

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
        if self.is_flipped:
            self.setPixmap(QPixmap(self.card.image_location()))
        else:
            path = os.getcwd() + "\\resources\\card_back.png"
            self.setPixmap(QPixmap(path))
        self.is_flipped = not self.is_flipped

    # Covered by another card; cannot be moved
    def is_covered(self):
        for card in self.parent().findChildren(QLabel):
            pos1 = self.pos()
            pos2 = card.pos()
            # In same pile and on top of pile
            if abs(pos1.x() - pos2.x()) == 0 and pos2.y() > pos1.y():
                if card.is_flipped or card.pos().x() < 120:
                    return True
        return False

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if not self.is_flipped and not self.is_covered():
            self.is_moving = True
            self.raise_()
            for card in self.parent().findChildren(QLabel):
                pos1 = self.pos()
                pos2 = card.pos()
                if abs(pos1.x() - pos2.x()) == 0 and pos2.y() > pos1.y():
                    self.cards_below.append(card)
                    card.raise_()

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.is_moving:
            # Moves the center of the top of card to the mouse
            self.move(self.mapToParent(ev.pos().__add__(QPoint(-50, -20))))

            # Moves the cards below the card
            times_to_add = 0
            for card in self.cards_below:
                card.move(self.mapToParent(ev.pos().__add__(QPoint(-50, 20 * times_to_add))))
                times_to_add += 1

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.is_moving = False
        prev_location = (self.position[0], self.position[1])

        # Searches for the closest card in the nearest pile
        closest_card = None
        for card in self.parent().findChildren(QLabel):
            if 39 > abs(card.pos().x() - self.pos().x()) > 0:
                if card.card.is_red() == self.card.is_red():
                    continue
                if card.card.face.value - self.card.face.value != 1:
                    continue
                if card.pos().x() < 120:
                    continue
                if card.is_flipped:
                    continue
                closest_card = card

        # If there is a card to move to
        moved = False
        if closest_card is not None:
            # Moves the card to its new location
            pos = closest_card.pos()
            self.move(pos.x(), pos.y() + 20)
            self.position = (pos.x(), pos.y() + 20)

            # Moves all the cards below to their new location
            times_to_add = 0
            for card in self.cards_below:
                times_to_add += 1
                prev_pos = self.pos().__add__(QPoint(-50, -75 + (20 * times_to_add)))
                card.move(self.mapToParent(prev_pos))
                card.position = (prev_pos.x(), prev_pos.y())

            self.cards_below.clear()
            moved = True

        # Handles King's being dropped in empty spaces
        if self.card.face == Face.KING:
            print("King should just drop into the spot and align.")
            moved = True

        # Moves all cards back if no available spot
        if not moved:
            self.move(self.position[0], self.position[1])
            for card in self.cards_below:
                card.move(card.position[0], card.position[1])
            self.cards_below.clear()
            return

        # Flips next card
        extra_card_pulled = False
        for card in self.parent().findChildren(QLabel):
            if prev_location[0] == card.pos().x():
                if prev_location[1] - 20 == card.pos().y() and card.is_flipped:
                    card.flip()
                    return
                elif card.pos().x() < 120:
                    # Handles Extra Card Pull
                    new_point = card.pos().__add__(QPoint(0, 20))
                    card.move(new_point)
                    card.position = (new_point.x(), new_point.y())
                    if extra_card_pulled:
                        print("Handling Extra Card Pull")
                        # CardImage(SolitaireSolver.s_deck.current_extra(), SolitaireSolver.solitaire_solver.cards, ...)
                        # Needs some way to get a QWidget that it can copy and delete
                        # Try to copy QWidget below where this one is supposed to go, then edit it

                        # Delete the card that was pulled from s_deck
                    continue
