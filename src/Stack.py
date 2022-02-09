from CardImage import *
from Node import *


class Stack:
    def __init__(self, is_discard=False):
        super().__init__()

        # Doubly Linked List Functionality
        self.head = None
        self.tail = None
        self.len = 0

        # Creates a discard Stack to discard drawn cards
        self.is_discard = is_discard
        if not is_discard:
            self.discard = Stack(True)

    # TODO: If len(draw_pile) < 3, prepend cards from draw_pile, if possible
    def draw_three(self):
        next_three = Stack()
        temp_head = self.discard.head
        for i in range(min(len(self), 3)):
            next_three.prepend(self.pop())
        while temp_head is not None and len(next_three) < 3:
            next_three.append(temp_head)
            temp_head = temp_head.prev
        return next_three

    def prepend(self, card: CardImage):
        if type(card) is Node:
            card = card.value

        # First card added to Stack
        if self.head is None:
            self.tail = Node(card)
            self.head = self.tail
            self.len = 1
            return

        # Links prev tail and next card to each other
        new_node = Node(card)
        new_node.next = self.tail
        self.tail.prev = new_node

        # Updates tail to new Node
        self.tail = new_node
        self.len += 1

    def append(self, card: CardImage):
        if type(card) is Node:
            card = card.value

        # First card added to Stack
        if self.head is None:
            self.tail = Node(card)
            self.head = self.tail
            self.len = 1
            return

        # Links prev and next card to each other
        new_node = Node(card)
        new_node.prev = self.head
        self.head.next = new_node

        # Updates head to new Node
        self.head = new_node
        self.len += 1

    # Popping from discard removes it permanently from the Stack
    def pop(self):
        # Gets current head
        head = self.head
        self.head = head.prev

        # Stack is empty
        if self.head is None:
            if self.is_discard:
                print("Discard stack is empty")
            else:
                print("Stack is empty")
            self.len = 0
            if not self.is_discard:
                self.discard.append(head)
            return head

        # Unlinks head from Stack
        head.prev = None
        self.head.next = None
        self.len -= 1

        # Adds head to discard Stack
        if not self.is_discard:
            self.discard.append(head.value)
        return head

    def reset(self):
        while self.discard.head is not None:
            self.append(self.discard.pop())

    def __str__(self):
        if len(self) == 0:
            return "Empty Stack."

        string = '['
        pointer = self.tail
        while pointer is not None:
            string += pointer.value.card.__str__() + ', '
            pointer = pointer.next
        return string[0:len(string) - 2] + ']\n'

    def __len__(self):
        return self.len
