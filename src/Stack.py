import CardImage
from CardImage import *
from Node import *


class Stack(list[CardImage]):
    def __init__(self):
        super().__init__()

        # Doubly Linked List Functionality
        self.head = None
        self.tail = None
        self.len = 0

    def draw_three(self):
        next_three = Stack()
        print(min(self.len, 3))
        for i in range(min(self.len, 3)):
            next_three.prepend(self.pop().value)
        return next_three

    def prepend(self, __object: CardImage):
        if type(__object) is not CardImage:
            return

        # First card added to Stack
        if self.head is None:
            self.tail = Node(__object)
            self.head = self.tail
            self.len = 1
            return

        # Links prev tail and next card to each other
        new_node = Node(__object)
        new_node.next = self.tail
        self.tail.prev = new_node

        # Updates tail to new Node
        self.tail = new_node

        self.len += 1

    def append(self, __object: CardImage):
        if type(__object) is not CardImage:
            return

        # First card added to Stack
        if self.head is None:
            self.tail = Node(__object)
            self.head = self.tail
            self.len = 1
            return

        # Links prev and next card to each other
        new_node = Node(__object)
        new_node.prev = self.head
        self.head.next = new_node

        # Updates head to new Node
        self.head = new_node

        self.len += 1

    def pop(self, __index=...):
        # Gets current head
        head = self.head
        self.head = head.prev

        # Stack is empty
        if self.head is None:
            self.len = 0
            return head

        # Unlinks head from Stack
        head.prev = None
        self.head.next = None

        self.len -= 1

        return head

    def __str__(self):
        string = '['
        pointer = self.tail
        while pointer is not None:
            string += pointer.value.card.__str__() + ', '
            pointer = pointer.next
        return string[0:len(string) - 2] + ']'

    def __len__(self):
        return self.len
