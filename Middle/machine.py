"""
Middle 2 Text Machine
"""

class VendingMachine:
    """ Empty VendingMachine class """

class TextMachine(VendingMachine):
    """ Main class for Text machine """

    def __init__(self, short:tuple[int], long:tuple[int]) -> None:
        """
        Init text machine values
        """
        self.prices = (short[1], long[1])
        self.counts = [short[0], long[0]]
        self.owe_values = [short[1], long[1]]

    def __str__(self) -> str:
        """
        String representation of self
        """
        return f'Text Machine:<{self.counts[0]} texts; ₴{self.prices[0]/100:.2f} each>'+\
                (f'; <{self.counts[1]} texts; ₴{self.prices[1]/100:.2f} each>' if self.counts[1] else '')


    def is_empty(self) -> bool:
        """ Check if Text machine is empty """
        return self.counts == [0,0]

    def texts_count(self) -> tuple[int]:
        """
        Return tuple with numbers of texts avaliable
        (short texts, long texts)
        """
        return tuple(self.counts)

    def still_owe(self) -> tuple[int]:
        """
        Return tuple with price still owed for the text
        (owe short, owe long)
        """
        return tuple(self.owe_values)

    def insert_money(self, inserted:tuple[str, int]):
        """
        Insert money to the text machine. Get presided result
        """
        given, tipe = inserted
        i = 0 if tipe == "short" else 1
        # machine has no texts of stated type
        if self.counts[i] == 0:
            return "Machine is empty", given
        #not enough money to buy a text
        if given < self.owe_values[i]:
            self.owe_values[i] -= given
            return f'Still owe ₴{self.owe_values[i]/100:.2f}', self.prices[i] - self.owe_values[i]
        # you can buy a text
        change = given - self.owe_values[i]
        self.owe_values[i] = self.prices[i]
        self.counts[i] -= 1
        # no change needed
        if change == 0:
            return  'Got a text!', self.owe_values[i]
        # gave to much add text info
        return 'Got a text!', change, (f'You can buy '
            f'{(change)//self.prices[1]} long text or '
            f'{(change)//self.prices[0]} short text')


    def stock_machine(self, text_numers:tuple[int, int]) -> None:
        """
        Add stated number of texts in machine
        """
        self.counts[0] += text_numers[0]
        self.counts[1] += text_numers[1]

    @staticmethod
    def railway_station_machine():
        """
        Return machine on railway station.
        With 200 short texts ₴2.25 each and
        200 long texts ₴3.45 each
        """
        return TextMachine((200,225), (200, 345))

    def __eq__(self, other: object) -> bool:
        """
        Self equels other if they have equel
        text numbers and owe values
        """
        return isinstance(other, TextMachine) and ((self.prices, self.counts,
                self.owe_values) == (other.prices, other.counts, other.owe_values))

    def __hash__(self) -> int:
        """
        Hashe self as tuple with text numbers and owe values
        """
        return hash((*self.prices, *self.counts, *self.owe_values))
