from SolitaireDeck import *

if __name__ == '__main__':
    deck = Deck().shuffle()
    s_deck = SolitaireDeck(deck)
    print(s_deck)
