"""
Lab 7.4 Document Exceptons
"""

class AbstractException(Exception):
    """ Basic class for class exceptions"""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class WrongInput(AbstractException):
    """ Invalid input """

class CursorRangeError(AbstractException):
    """ Cursor out of range """

class CallHomeError(AbstractException):
    """ Unable to call home method """

class CallEndError(AbstractException):
    """ Unable to call end method """

class FileWrongName(AbstractException):
    """ Unable to create file """



class Document:
    """ Class with information methods to work with the document """

    def __init__(self) -> None:
        """
        Init class values with empty row and cursor
        """
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = 'example.txt'

    def insert(self, character:str) -> None:
        """
        Insert character on current cursor position
        """
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()


    def delete(self):
        """
        Delete character on cursor
        """
        if len(self.characters) == 0:
            raise CursorRangeError("There are no character to delete")
        del self.characters[self.cursor.position]


    def save(self) -> None:
        """
        Write document information into the file
        """
        if self.filename == '':
            raise FileWrongName("Invalid file name")

        with open(self.filename, "w", encoding='utf-8') as file:
            file.write("".join((str(c) for c in self.characters)))

    @property
    def string(self) -> str:
        """
        String. Return the document's test
        """
        return "".join((str(c) for c in self.characters))


class Cursor:
    """
    Cursor class
    """
    def __init__(self, document:Document) -> None:
        """
        Init cursor values with default position as 0
        """
        self.document = document
        self.position = 0

    def forward(self) -> None:
        """
        Move forward on 1 character.
        Raise: CursorRangeError if it is last position
        """
        if self.position == len(self.document.characters):
            raise CursorRangeError( "It is the last position, you can't move forward")
        self.position += 1

    def back(self) -> None:
        """
        Move back on 1 character.
        Raise: CursorRangeError if it is the first position
        """
        if self.position == 0:
            raise CursorRangeError("It is in the first position, you can't move back")
        self.position -= 1

    def home(self):
        """
        Change cursor position to the first one in a row
        """
        if len(self.document.characters) == 0:
            raise CallHomeError( "Unable to use method on empty document")

        while self.position and self.document.characters[self.position - 1].character != "\n":
            self.position -= 1

    def end(self):
        """
        Change cursor position to the last one in a row
        """
        if len(self.document.characters) == 0:
            raise CallEndError( "Unable to use method on empty document")

        while (self.position < len(self.document.characters))\
                and (self.document.characters[self.position].character != "\n"):
            self.position += 1


class Character:
    """
    One character class provides different styles
    """

    def __init__(self, character, bold=False, italic=False, underline=False):
        """
        Init character values without additional text style as default.
        """
        if len(character) != 1:
            raise WrongInput("Invlid input character")
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """
        String representation of the character
        """
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character
