"""
Lab 4.5 Wanderer game
Organize the game
"""


class Room:
    """
    Room class with its data
    """

    def __init__(self, name: str) -> None:
        """
        Init values with default description, character and item as None.
        And default linked rooms as dict()
        """
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, description: str) -> None:
        """
        Set room description
        """
        self.description = description

    def link_room(self, room, direction: str) -> None:
        """
        Function that links rooms with sides of the world
        """
        self.linked_rooms[direction] = room

    def set_character(self, character) -> None:
        """
        Set the character into the room
        """
        self.character = character

    def get_character(self) -> object:
        """
        Return rooms character
        """
        return self.character

    def set_item(self, item) -> None:
        """
        Set the item into the room
        """
        self.item = item

    def get_item(self) -> object:
        """
        Return room's item
        """
        return self.item

    def get_details(self) -> None:
        """
        Print room information string
        """
        print(self.name, '--------------------', self.description, sep='\n')
        for direction, room in self.linked_rooms.items():
            print(f'The {room.name} is {direction}')

    def move(self, direction: str) -> object:
        """
        Move to another room on stated direction
        """
        return self.linked_rooms[direction]


class Enemy:
    """
    Enemy class with DEFEATED constnant
    """
    DEFEATED = 0

    def __init__(self, name: str, description: str) -> None:
        """
        Init class values with starting conversation and weakness as None
        """
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation: str) -> None:
        """
        Set conversation for class object
        """
        self.conversation = conversation

    def set_weakness(self, weakness: str) -> None:
        """
        Set weakness for class object
        """
        self.weakness = weakness

    def describe(self) -> None:
        """
        Print information about the enemy
        """
        print(f'{self.name} is here!\n{self.description}')

    def talk(self) -> None:
        """
        Print enemy conversation string
        """
        print(self.conversation)

    def fight(self, fight_with) -> bool:
        """
        Return fight battle result
        """
        return self.weakness is None or (fight_with == self.weakness)

    def get_defeated(self) -> int:
        """
        Defeat the enemy. Change DEFEATED value
        """
        Enemy.DEFEATED += 1
        return Enemy.DEFEATED


class Item:
    """
    Item class with information
    related to the one item
    """

    def __init__(self, name:str) -> None:
        """
        Init values with default description as None
        """
        self.name = name
        self.description = None


    def set_description(self, description):
        """
        Function to set the description for the item
        """
        self.description = description

    def describe(self):
        """
        Print information about the item
        """
        print(f"The {self.name} is here! - {self.description}")

    def get_name(self):
        """
        Return items name
        """
        return self.name
