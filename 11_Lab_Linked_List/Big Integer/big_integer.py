"""
Lab 11 task 3
Big integers implemented by double linked list
"""


class Node:
    """
    Two way node class for double linked list data sructure
    """

    def __init__(self, data, previous = None, following = None):
        """Instantiates a TwoWayNode with default next and previous of None"""
        self.data = data
        self.left = previous
        self.right = following

    def __str__(self) -> str:
        """
        return sting with node data and data of left and right nodes
        """
        return f'Node( data={self.data}, left= {self.left.data if self.left is not None else None},\
 right= {self.right.data if self.right is not None else None} )'


class BigInteger:
    """
    Class with oparations for biginteger
    """

    def __init__(self, string='0') -> None:
        if string[0] == '-':
            self.is_negative = True
            self.length = len(string) - 1
            self.create_linked_list(string[1:])
        else:
            self.is_negative = False
            self.length = len(string)
            self.create_linked_list(string)

    def negative(self):
        """
        check if number is negative
        """
        return self.is_negative

    def positive(self):
        """
        check if number is positive
        """
        return not self.is_negative

    def __len__(self):
        """
        return length of the linked list
        """
        return self.length

    def __repr__(self) -> str:
        """
        Representation method
        """
        return f"BigInteger({str(self)})"

    def __str__(self) -> str:
        """
        return string with big integer
        """
        output = ['-'] if self.negative() else []
        current = self.head
        while current is not None:
            output.append(str(current.data))
            current = current.right
        return ''.join(output)

    def to_string(self):
        """
        return biginteger as string
        """
        return str(self)

    def create_linked_list(self, string:str):
        """
        Create two way linked list with
        two pointers in the head and tail
        """
        self.tail = Node(int(string[0]), None, None)
        self.head = self.tail

        for i in range(1, len(string)):
            prev = self.tail
            self.tail = Node(int(string[i]), prev, None)
            prev.right = self.tail


    def insert_tail(self, digit):
        """
        insert value in the tail of the linked list
        """
        new_node = Node(digit,self.tail, None)
        self.tail.right = new_node
        self.tail = new_node

    def insert_head(self, digit):
        """
        insert value in the head of the linked list
        """
        new_node = Node(digit, None, self.head)
        self.head.left = new_node
        self.head = new_node

    def extend_tail(self, other:object):
        """
        extend list with adding new objects in the tail
        """
        other.head.left = self.tail
        self.tail.right = other.head
        self.tail = other.tail

    def extend_head(self, other:object):
        """
        extend list with adding new objects in the head
        """
        self.head.left = other.tail
        other.tail.right = self.head
        self.head = other.head



# -----------------------------------------------------------------------------
# ----------------------------- COMPARABLE OPERATORS --------------------------
# -----------------------------------------------------------------------------

    def __eq__(self, other: object):
        """
        Operator equal (==)
        """
        if len(self) != len(other) or self.negative() != other.negative():
            return False
        cur_self, cur_other = self.head, other.head
        while cur_self is not None:
            if cur_other.data != cur_self.data:
                return False
            cur_self, cur_other = cur_self.right, cur_other.right
        return True

    def __ne__(self, other: object) -> bool:
        """
        Operator not equel (!=)
        """
        return not self==other

    def __gt__(self, other:object) -> bool:
        """
        Greater than operator (>)
        """
        if len(self)!= len(other):
            return (len(self) > len(other)) == self.positive()
        if self.negative() != other.negative():
            return self.negative() > other.negative()
        cur_self, cur_other = self.head,other.head
        while cur_self is not None:
            if cur_self.data != cur_other.data:
                return (cur_self.data > cur_other.data) == self.positive()
            cur_self, cur_other = cur_self.right, cur_other.right
        return False

    def __le__(self, other:object) -> bool:
        """
        Operator less or equal (<=)
        """
        return not self > other

    def __lt__(self, other: object) -> bool:
        """
        Operator less than (<)
        """
        if len(self)!= len(other):
            return (len(self) < len(other)) == self.positive()
        if self.negative() != other.negative():
            return self.negative() < other.negative()
        cur_self, cur_other = self.head,other.head
        while cur_self is not None:
            if cur_self.data != cur_other.data:
                return (cur_self.data < cur_other.data) == self.positive()
            cur_self, cur_other = cur_self.right, cur_other.right
        return False

    def __ge__(self, other:object) -> bool:
        """
        Operator less or equal (>=)
        """
        return not self < other


# -----------------------------------------------------------------------------
# ----------------------------- ARITHMETIC OPERATORS --------------------------
# -----------------------------------------------------------------------------



    def simple_sum(self, other):
        """
        Sum of 2 positive bigintegers
        """

        # find which number has bigger length
        less, more = other.tail, self.tail if len(self)>len(other) else \
                     self.tail, other.tail

        # create new biginteger with right last number
        add_part = less.data + more.data
        add_one, new_digit = divmod(add_part, 10)
        new_integer = BigInteger(str(new_digit))

        #Aadd digits in the head as sum of two current last
        # digits of more and less. Take into accout add_one
        while less is not None:
            add_part = less.data + more.data + add_one
            add_one, new_digit = divmod(add_part, 10)
            new_integer.insert_head(new_digit)
            less, more = less.left, more.left
        # less number ended add digits from more number
        while more is not None:
            add_part = more.data + add_one
            add_one, new_digit = divmod(add_part, 10)
            new_integer.insert_head(new_digit)
            more = more.left

        # add 1 in head when after iteration there is saved one
        # e.x. more = 9998, less = 11, new_integer = 0009 and saved one -> new_integer = 10009
        if add_one:
            new_integer.insert_head(1)
        return new_integer

    def __add__(self, other:object):
        """
        Adding of two big integers. Save in new class object
        """


        if self.negative() != other.negative():
            pass

        ansver = self.simple_sum(other)

        ansver.is_negative = self.negative()
        return ansver


    def __sub__(self, other:object):
        """
        Substraction operator (self - other)
        """
        if self.negative() and other.positive():
            ansver = self.simple_sum(other)
            ansver.is_negative = True
        elif self.negative() and other.positive():
            pass


        elif self.positive() and other.negative():
            pass

        return ansver

    def simple_sub(self, other):
        """
        Substraction of two bigintegers
        supposed that self > other >= 0
        """

        while len(other) != len(self):
            other.insert_head(0)
        more , less = self.tail, other.tail

        digit = more.data - less.data
        minus_one = 0
        if digit <0:
            digit +=10
            minus_one = -1
        result = BigInteger(digit)

        while less is not None:
            break

        result.clear_nulls()


    def clear_nulls(self):
        """
        Remome zeros from the begging of the biginteger
        """
        while self.head.data == 0 and self.head.next is not None:
            self.head = self.head.right
            self.head.left.right = None
            self.head.left = None


