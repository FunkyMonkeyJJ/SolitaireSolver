from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QFrame

from Card import *


# Replaces the current QLabel on the GUI, links information
# to the new QLabel, and creates custom events
class CardImage(QLabel):
    def __init__(self, card, parent, widget, solitaire_solver, replace=True):
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
        self.setObjectName(widget.objectName())
        self.setGeometry(widget.geometry())
        self.position = (self.geometry().x(), self.geometry().y())

        # Replaces my static use of SolitaireSolver before
        self.solitaire_solver = solitaire_solver

        # Deletes the base widget from the GUI
        if replace:
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
        for card in self.parent().findChildren(CardImage):
            # In same pile and on top of pile
            if abs(self.x() - card.x()) == 0 and card.y() > self.y():
                if card.isEnabled() and (card.is_flipped or card.x() < 120):
                    return True
        return False

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.is_flipped and self.x() < 120:
            # Handle clicking the extra card pile
            # i = 0
            print("CLICKED!")
            # TODO: Now that the cards will not repeat without breaking, and you always press the reset button
            #  you need to make it so that the number of cards that can't be repeated are found and pushed back to the
            #  top of the extra pile
            extra_cards = self.solitaire_solver.extra_cards
            next_three = extra_cards.draw_three()

            # print(len(next_three))
            # print(len(extra_cards))
            # Might need to pop and move the card around because it is being moved in next_three, but not extra_cards
            if len(next_three) == 2 and len(extra_cards) > 2:
                # Add one card back to the next three
                next_three.insert(0, extra_cards[2])
            elif len(next_three) == 1:
                if len(extra_cards) > 2:
                    # Add two cards back to the next three
                    next_three.insert(0, extra_cards[2])
                    next_three.insert(0, extra_cards[1])
                elif len(extra_cards) > 1:
                    # Add one card back to the next three
                    next_three.insert(0, extra_cards[1])

            for i in range(len(next_three)):
                card = next_three.pop().value
                # for card in next_three:
                #     if card == extra_cards.tail.value and i > 0:
                #         print("Card == tail")
                #         break
                # if len(extra_cards) > 2:
                #     first_card_back = extra_cards[2]
                #     first_card_back.move(20, 180)
                # elif len(extra_cards) > 1:
                #     first_card_back = extra_cards[1]
                #     first_card_back.move(20, 210)
                # print(card.card)
                card.move(20, 180 + (30 * i))
                card.position = (card.x(), card.y())
                card.flip()
                card.raise_()
                i += 1
        elif not self.is_flipped and not self.is_covered():
            # Prepares card for moving
            self.is_moving = True
            self.raise_()

            # Prevents Ace's from being moved from suits piles
            if self.card.face == Face.ACE and self.x() > 880:
                self.is_moving = False
                return

            # Prepares the cards below the card for moving
            for card in self.parent().findChildren(CardImage):
                if abs(self.x() - card.x()) == 0 and card.y() > self.y():
                    self.cards_below.append(card)
                    card.raise_()

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.is_moving:
            # Moves the center of the top of card to the mouse
            self.move(self.mapToParent(ev.pos().__add__(QPoint(-50, -30))))

            # Moves the cards below the card
            times_to_add = 0
            for card in self.cards_below:
                card.move(self.mapToParent(ev.pos().__add__(QPoint(-50, 30 * times_to_add))))
                times_to_add += 1

    # TODO: Last thing to do is to cycle through the extra pile and end the game
    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        if not self.is_moving:
            return
        print("Released!")

        # Searches for the closest card in the nearest pile
        closest_card = None
        laying_on_suits = False
        for card in self.parent().findChildren(QLabel):
            if closest_card is not None:
                break
            if 39 > abs(card.x() - self.x()) > 0:
                if card.x() < 120:
                    continue
                if card.x() > 880:
                    if len(self.cards_below) > 0:
                        continue

                    if card.y() == 20 and self.card.suit == Suit.SPADES:
                        closest_card = card
                    elif card.y() == 180 and self.card.suit == Suit.HEARTS:
                        closest_card = card
                    elif card.y() == 340 and self.card.suit == Suit.CLUBS:
                        closest_card = card
                    elif card.y() == 500 and self.card.suit == Suit.DIAMONDS:
                        closest_card = card
                    else:
                        continue

                    laying_on_suits = True
                    continue
                if card.card.is_red() == self.card.is_red():
                    continue
                if card.card.face.value - self.card.face.value != 1:
                    continue
                if card.is_flipped:
                    continue
                closest_card = card

        # If there is a card to move to
        moved = False
        if closest_card is not None and not laying_on_suits:
            # Moves the card to its new location
            self.move(closest_card.x(), closest_card.y() + 30)
            self.position = (closest_card.x(), closest_card.y() + 30)

            # Moves all the cards below to their new location
            times_to_add = 1
            for card in self.cards_below:
                times_to_add += 1
                prev_pos = closest_card.pos().__add__(QPoint(0, 30 * times_to_add))
                card.move(prev_pos)
                card.position = (prev_pos.x(), prev_pos.y())

            self.cards_below.clear()
            moved = True

        # Handles King's being dropped in empty spaces
        if self.card.face == Face.KING:
            for x_coord in [140, 260, 380, 500, 620, 740, 860]:
                if abs(self.x() - x_coord) <= 20:
                    card_in_spot = False
                    for card in self.parent().findChildren(QLabel):
                        if card.x() == x_coord and card.y() == 20:
                            card_in_spot = True

                    if not card_in_spot and self.position[0] != x_coord:
                        self.move(x_coord, 20)
                        self.position = (self.x(), self.y())

                        # Moves all the cards below to their new location
                        times_to_add = 0
                        for card in self.cards_below:
                            times_to_add += 1
                            card.move(self.pos().__add__(QPoint(0, 30 * times_to_add)))
                            print(card.pos())
                            card.position = (card.x(), card.y())

                        self.cards_below.clear()
                        moved = True

        # Handles placing on suits piles
        if laying_on_suits:
            try:
                if self.card.face == Face.ACE:
                    self.move(closest_card.x(), closest_card.y())
                    self.position = (self.x(), self.y())
                    closest_card.setParent(None)
                    moved = True
                elif self.card.face.value - closest_card.card.face.value == 1:
                    self.move(closest_card.x(), closest_card.y())
                    self.position = (self.x(), self.y())
                    moved = True
                # TODO: Check each suit pile to determine if all are full, then end if they are
            except:
                pass

        # Moves all cards back if no available spot
        if not moved:
            self.move(self.position[0], self.position[1])
            for card in self.cards_below:
                card.move(card.position[0], card.position[1])
            self.cards_below.clear()
            return

        # Cycles next card if not the first pull
        extra_cards = self.solitaire_solver.extra_cards
        if extra_cards.__contains__(self):
            if len(extra_cards) > 3:
                if extra_cards[3].y() == 20:
                    self.solitaire_solver.extra_cards.remove(self)
                    return

                third_card_back = extra_cards[3]
                third_card_back.move(20, 180)
                third_card_back.position = (20, 180)

                second_card_back = extra_cards[2]
                second_card_back.move(20, 210)
                second_card_back.position = (20, 210)

                first_card_back = extra_cards[1]
                first_card_back.move(20, 240)
                first_card_back.position = (20, 240)

            self.solitaire_solver.extra_cards.remove(self)
