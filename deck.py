from character import Character
from character_type import CharacterType
from location import Location
from random import shuffle


class Deck:
    def __init__(self):
        self.deck = []
        self.populate_deck()
        self.shuffle()

    def populate_deck(self):
        for i in range(0, 3):
            self.deck.append(Character(CharacterType.ambassador, Location.deck))
        for i in range(0, 3):
            self.deck.append(Character(CharacterType.assassin, Location.deck))
        for i in range(0, 3):
            self.deck.append(Character(CharacterType.captain, Location.deck))
        for i in range(0, 3):
            self.deck.append(Character(CharacterType.contessa, Location.deck))
        for i in range(0, 3):
            self.deck.append(Character(CharacterType.duke, Location.deck))

    def shuffle(self):
        shuffle(self.deck)

    def draw(self):
        assert len(self.deck) > 0, "Error: an attempt was made to draw from an empty deck."
        return self.deck.pop(-1)

    def add_and_shuffle(self, *cards):
        for card in cards:
            assert isinstance(card, Character), "Error: an attempt was made to add a non-Character to the deck."
            self.deck.append(card)
        self.shuffle()

    def exchange(self, card_for_deck):
        assert isinstance(card_for_deck, Character), "Error: an attempt was made to exchange a non-Character with the " \
                                                     "deck."
        self.add_and_shuffle(card_for_deck)
        return self.draw()
