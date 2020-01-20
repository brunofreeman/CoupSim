from location import Location
from character_type import CharacterType
from action import Action
from counteraction import Counteraction


class Character:
    def __init__(self, character_type, location):
        self.character_type = character_type
        self.location = location

    def lose_influence(self):
        assert self.location == Location.influence, "Error: a character that was not in the influence position was " \
                                                    "instructed to lose influence. "
        self.location = Location.face_up

    def has_action(self, action):
        if action == Action.income or action == Action.foreign_aid or action == Action.coup:
            return True

        if self.character_type == CharacterType.duke:
            return action == Action.tax

        if self.character_type == CharacterType.assassin:
            return action == Action.assassinate

        if self.character_type == CharacterType.ambassador:
            return action == Action.exchange

        if self.character_type == CharacterType.captain:
            return action == Action.steal

        return False

    def has_counteraction(self, counteraction):
        if self.character_type == CharacterType.duke:
            return counteraction == Counteraction.block_foreign_aid

        if self.character_type == CharacterType.ambassador or self.character_type == CharacterType.captain:
            return counteraction == Counteraction.block_stealing

        if self.character_type == CharacterType.contessa:
            return counteraction == Counteraction.block_assassination

        return False

'''
    def exchange_with_deck(self):
        assert self.location == Location.influence, "Error: a character that was not in the influence position was instructed to exchange with the deck."
        self.add_to_deck()
        self.deck.shuffle()
        new_character = self.deck.draw()
        self.character_type = new_character.character_type
'''
