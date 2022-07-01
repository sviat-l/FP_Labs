"""
Lab 7.3 Auth NoteBook
"""

import datetime

# Store the next available id for all new notes
LAST_ID = 0


class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''

    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global LAST_ID
        LAST_ID += 1
        self.id = LAST_ID

    def match(self, filter: str):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags.'''
        return filter in self.memo or filter in self.tags


class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self) -> None:
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo: str, tags: str = '') -> None:
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id: int, memo: str) -> None:
        '''Find the note with the given id and change its
        memo to the given value.'''
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id: int, tags: str) -> None:
        '''Find the note with the given id and change its
        tags to the given value.'''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter: str) -> list:
        '''Find all notes that match the given filter
        string.'''
        return [note for note in self.notes if
                note.match(filter)]

    def __str__(self) -> str:
        """ String representation of self """
        return ('\n'.join(["{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo) for note in self.notes]))



class Menu:
    '''Display a menu and respond to choices when run.'''

    def __init__(self):
        """Init values for menu, choice ooptions and empt Notebook"""
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        """Display information about the menu"""
        print("""
    Notebook Menu
    1. Show all Notes
    2. Search Notes
    3. Add Note
    4. Modify Note
    5. Quit
    """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes: Note = None):
        """ Show all notes in the notebook"""
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo))

    def search_notes(self):
        """ Ask user to print a note name. Search for note in note book"""
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        """Ask user to print the note and add it to the notebook"""
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        """ modify note, memo or tags informtion"""
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        """ quit the program"""
        print("Thank you for using your notebook today.")
        raise SystemExit


if __name__ == "__main__":
    Menu().run()
