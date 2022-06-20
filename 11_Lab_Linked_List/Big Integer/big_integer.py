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
    Class with oparations for biginteger nubmers
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

# -----------------------------------------------------------------------------

    def insert_tail(self, digit:int):
        """
        insert value in the tail of the linked list
        """
        new_node = Node(digit,self.tail, None)
        self.tail.right = new_node
        self.tail = new_node
        self.length += 1

    def insert_head(self, digit:int):
        """
        insert value in the head of the linked list
        """
        new_node = Node(digit, None, self.head)
        self.head.left = new_node
        self.head = new_node
        self.length += 1

    def extend_tail(self, other:object):
        """
        extend list with adding new objects in the tail
        """
        other.head.left = self.tail
        self.tail.right = other.head
        self.tail = other.tail
        self.length += len(other)

    def extend_head(self, other:object):
        """
        extend list with adding new objects in the head
        """
        self.head.left = other.tail
        other.tail.right = self.head
        self.head = other.head
        self.length += len(other)

    def lpop(self):
        """
        Remove last element from the object
        """
        prev = self.tail
        self.tail = prev.left
        self.tail.right, prev.left = None, None
        self.length -= 1

    def fpop(self):
        """
        Remove first element from the object
        """
        prev = self.head
        self.head = prev.right
        self.head.left, prev.rigth = None, None
        self.length -= 1

    def notzero(self):
        """
        Check if number is not zero
        """
        return self.head.data != 0

# -----------------------------------------------------------------------------
# ----------------------------- COMPARABLE OPERATORS --------------------------
# -----------------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
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
        if self.negative() != other.negative():
            return self.negative() < other.negative()
        if len(self)!= len(other):
            return (len(self) > len(other)) == self.positive()
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
        if self.negative() != other.negative():
            return self.negative() > other.negative()
        if len(self)!= len(other):
            return (len(self) < len(other)) == self.positive()
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

    def abs_biginteger(self):
        """
        Return absolute value of BigInteger as new object
        """
        result =  BigInteger(str(self))
        result.is_negative = False
        return result

    def gt_abs(self, other:object) -> bool:
        """
        Greater than abs function. Compare two Bigdigits absolute values
        Return:
            True if abs(self) > abs(other)
            False if abs(self) < abs(other)
            None if abs(self) == abs(other)
        """
        # same sign
        if self.positive() == other.positive():
            if self==other:
                return None
            return self.positive() == (self > other)
        # different length
        if len(self) != len(other):
            return len(self) > len(other)
        # different sign, the same length
        first, second = self.head, other.head
        while first is not None:
            if first.data  != second.data:
                return first.data > second.data
            first, second = first.right, second.right
        return None


# -----------------------------------------------------------------------------
# ----------------------------- ARITHMETIC OPERATORS --------------------------
# -----------------------------------------------------------------------------


    def simple_sum(self, other:object):
        """
        Sum of 2 bigintegers absolute values

        """
        # find which number has bigger length set initial values
        less, more = (other.tail, self.tail) if len(self)>len(other) else \
                     (self.tail, other.tail)
        add_one, new_integer = 0, BigInteger()

        #add digits in the head as sum of two current last
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
        # remove initial extra zero from the result
        new_integer.lpop()
        return new_integer

    def simple_sub(self, other:object):
        """
        Substraction of two bigintegers
        supposed that self > other >= 0
        """
        more, less = self.tail, other.tail
        minus_one, result = 0, BigInteger()

        # iterate on BigIntegers to the head. Substract digits one after another
        while less is not None:
            digit = more.data - less.data - minus_one
            minus_one, digit = (0, digit) if digit>-1  else (1, digit+10)
            result.insert_head(digit)
            less, more = less.left, more.left
        # smaller number calculated work only with bigger
        while more is not None:
            digit = more.data - minus_one
            minus_one, digit = (0, digit) if digit>-1  else (1, digit+10)
            result.insert_head(digit)
            more = more.left
        # remove initial extra zero from the result
        result.lpop()
        # Remome zeros from the begging of the biginteger
        while result.head.data == 0 and result.head.right is not None:
            result.fpop()
        return result


    def __add__(self, other:object):
        """
        Adding of two big integers. Save in new class object
        """
        # same signs
        if self.positive() == other.positive():
            ansver = self.simple_sum(other)
            ansver.is_negative = self.negative()
        # Different signs. Compare absolute values
        elif self.positive():
            if self.gt_abs(other):
                ansver = self.simple_sub(other)
            else:
                ansver = other.simple_sub(self)
                ansver.is_negative = True
        else:
            if self.gt_abs(other):
                ansver = self.simple_sub(other)
                ansver.is_negative = True
            else:
                ansver = other.simple_sub(self)
        return ansver

    def __sub__(self, other: object):
        """
        Substraction operator (self - other)
        """
        if self.negative() and other.positive():
            ansver = self.simple_sum(other)
            ansver.is_negative = True
        elif self.positive() and other.negative():
            ansver = self.simple_sum(other)
        elif self == other:
                return BigInteger('0')
        # both positive
        elif self.positive():
            if self > other:
                ansver = self.simple_sub(other)
            else:
                ansver = other.simple_sub(self)
                ansver.is_negative = True
        # both negative
        else:
            if self < other:
                ansver = self.simple_sub(other)
                ansver.is_negative = True
            else:
                ansver = other.simple_sub(self)
        return ansver

# -----------------------------------------------------------------------------

    def __mul__(self, other:object):
        """
        Multiplication operator
        """
        result = BigInteger('0')
        current = other.tail
        i = 0
        while current is not None:
            if current.data:
                digit_result = BigInteger('0')
                # multiply by current digit
                for _ in range(current.data):
                    digit_result += self
                # consider current possition (*10**x)
                for _ in range(i):
                    digit_result.insert_tail(0)

                result += digit_result
            current, i = current.left, i+1
        # Get sign value. Consider initial numbers and result != 0
        result.is_negative = (self.negative() == other.positive()) and result.notzero()
        return result

    def __pow__(self, other:object):
        """
        Power operator
        """
        # extreme examples
        if not other.notzero():
            return BigInteger('1')
        if len(self) ==1 and self.head.data in [0,1]:
            return BigInteger(str(self.head.data))
        result = BigInteger('1')
        current_pow = self
        # bit representation of degree
        degree_in_bit = other.into_bin()
        current_bit = degree_in_bit.tail
        first_bit = current_bit.data
        # iterate on degree bit representation. That is easier and faster to calculate
        # e.x find: x**7 = x**(4+2+1) = x**1 * x**2  * x**4 =x**1 * (x**1)**2 * (x**2)**2
        while current_bit is not None:
            if current_bit.data:
                result *= current_pow
            current_pow = current_pow * current_pow
            current_bit = current_bit.left
        # set sigh value
        if self.negative() and first_bit:
            result.is_negative = True
        return result


    def __floordiv__(self, other:object):
        """
        Floor division operator (//)
        """
        # set initial values
        remainder = self.abs_biginteger()
        modul, modul_was_negative = other, other.negative()
        modul.is_negative, quotient = False, BigInteger()

        # substitute while remainder is more than modul
        while remainder >= modul:
            remainder = remainder.simple_sub(modul)
            quotient += BigInteger('1')

        # Modify result considering numbers sighs
        if self.negative() != modul_was_negative:
            if remainder.notzero():
                quotient += BigInteger('1')
            quotient.is_negative = True

       # set initial modular (other) sigh
        if modul_was_negative:
            other.is_negative = True

        return quotient

    def __mod__(self, other:object):
        """
        Modular operator (%)
        """
        # set initial values
        remainder = self.abs_biginteger()
        modul, modul_was_negative = other, other.negative()
        modul.is_negative = False

        # substitute while number is more than modul
        while remainder >= modul:
            remainder = remainder.simple_sub(modul)

        # Modify result considering number sighs
        if self.negative()!= modul_was_negative and remainder.notzero() :
            remainder =  remainder - modul
        if self.negative():
            remainder.is_negative = not remainder.is_negative

        # set initial modular (other) sigh
        if modul_was_negative:
            other.is_negative = True
        return remainder

    def big_divmod(self, other:object):
        """
        Find quotient and remainder of (self, other), return tuple (div, mod)
        """
        # set initial values
        remainder, quotient = self.abs_biginteger(), BigInteger()
        modul, modul_was_negative = other, other.negative()
        modul.is_negative = False

        # substitute while remainder is more than modul
        ## Not rational ##
        while remainder >= modul:
            remainder = remainder.simple_sub(modul)
            quotient += BigInteger('1')

        # Modify quotient and remainder considering numbers signs
        if self.negative() != modul_was_negative:
            if remainder.notzero():
                quotient += BigInteger('1')
                remainder =  remainder - modul
            quotient.is_negative = True
        if self.negative() and remainder.notzero():
            remainder.is_negative = not remainder.is_negative

        # set initial modular (other) sigh
        if modul_was_negative:
            other.is_negative = True
        return quotient, remainder


# -----------------------------------------------------------------------------
# ------------------------------ BITWISE OPERATORS ----------------------------
# -----------------------------------------------------------------------------


    def bin_into_integer(self):
        """
        Return BigInteger by its binary representation
        """
        # set constants and initial values
        ansver, current_pow,  = BigInteger(), BigInteger('1')
        current, big_2 = self.tail, BigInteger('2')
        # Iterate on bin string. Increase 2 degree
        while current is not None:
            if current.data:
                ansver += current_pow
            current_pow, current =  current_pow * big_2, current.left
        return ansver

    def into_bin(self):
        """
        Return bit representation of BigInteger
        !! Works only for positive numbers !!
        """
        # set constants and initial values
        curr_number, ansver = BigInteger(str(self)), BigInteger()
        big_0, big_2 = BigInteger('0'), BigInteger('2')
        # Find divmod values. Redefine number as number // 2
        while curr_number > big_0:
            curr_number, current_bit = curr_number.big_divmod(big_2)
            ansver.insert_head(current_bit.head.data)
        # remove initial last digit
        ansver.lpop()
        return ansver

    def __rshift__(self, other:object):
        """
        Bitwise right shift operator
        """
        result = self.into_bin()
        for _ in range(int(str(other))):
            result.lpop()
        return result.bin_into_integer()

    def __lshift__(self, other:object):
        """
        Bitwise left shift operator
        """
        result = self.into_bin()
        for _ in range(int(str(other))):
            result.insert_tail(0)
        return result.bin_into_integer()

    def __and__(self, other:object):
        """
        Bitwise AND (&) operator (only for positive)
        """
        # set initial values
        self_bit = self.into_bin()
        other_bit = other.into_bin()
        result = BigInteger()
        less, more = (other_bit.tail, self_bit.tail) if len(self_bit)>len(other_bit)\
                else (self_bit.tail, other_bit.tail)
        # compare bits successively
        while less is not None:
            result.insert_head( less.data & more.data)
            less, more = less.left, more.left
        # remove initial extra digit
        result.lpop()
        return result.bin_into_integer()

    def __xor__(self, other:object):
        """
        Bitwise XOR (^) operator (only for positive)
        """
        # set initial values
        self_bit = self.into_bin()
        other_bit = other.into_bin()
        result = BigInteger()
        less, more = (other_bit.tail, self_bit.tail) if len(self_bit)>len(other_bit)\
                else (self_bit.tail, other_bit.tail)
        # compare bits successively
        while less is not None:
            result.insert_head( less.data ^ more.data)
            less, more = less.left, more.left
        # add bits from binary number with bigger order
        while more is not None:
            result.insert_head(more.data)
            more = more.left
        # remove initial extra digit
        result.lpop()
        return result.bin_into_integer()

    def __or__(self, other:object):
        """
        Bitwise OR (|) operator (only for positive)
        """
        # set initial values
        self_bit = self.into_bin()
        other_bit = other.into_bin()
        result = BigInteger()
        less, more = (other_bit.tail, self_bit.tail) if len(self_bit)>len(other_bit)\
                else (self_bit.tail, other_bit.tail)
        # compare bits successively
        while less is not None:
            result.insert_head( less.data | more.data)
            less, more = less.left, more.left
        # add bits from binary number with bigger order
        while more is not None:
            result.insert_head(more.data)
            more = more.left
        # remove initial extra digit
        result.lpop()
        return result.bin_into_integer()
