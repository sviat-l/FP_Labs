"""
Lab 6.3 Book
"""

class Book:
    """ Class with data and method related to the book """

    def __init__(self, name:str, author:str, page_num:int) -> None:
        """ Init book values with current_page default as 1, and bookmark as None """
        self.name = name
        self.author = author
        self.page_num = page_num
        self.current_page = 1
        self.bookmarked_page = None

    def __str__(self) -> str:
        """
        String representaion of self
        """
        return f'Book<{self.name} by {self.author}: {self.page_num} page'\
        f'{"" if self.page_num == 1 else "s"}, currently on page {self.current_page}' + \
        (f', page {self.bookmarked_page} bookmarked' if self.bookmarked_page is not None else '')\
            +'>'

    def turn_page(self, change_number:int):
        """
        Change current page number.
        If change_number < 0 turn pages backwards.
        Keep current page number from 1 to book page number
        """
        self.current_page += change_number
        self.current_page = max(self.current_page, 1)
        self.current_page = min(self.current_page, self.page_num)

    def get_current_page(self):
        """ Return current page in the book """
        return self.current_page

    def place_bookmark(self):
        """ Place bookmark on the current page """
        self.bookmarked_page = self.current_page

    def remove_bookmark(self):
        """ Remove bookmark from the book """
        self.bookmarked_page = None

    def get_bookmarked_page(self):
        """ Return bookmarked page of the book """
        return self.bookmarked_page

    def turn_to_bookmark(self):
        """ Change current page to bookmarked one """
        if self.bookmarked_page is not None:
            self.current_page = self.bookmarked_page

    def __eq__(self, other: object) -> bool:
        """ Check if self equels other """
        return (self.name, self.author, self.page_num, self.current_page, self.bookmarked_page) ==\
            (other.name, other.author, other.page_num, other.current_page, other.bookmarked_page)
