def get_number():
    """
    Return number
    """
    number = 82
    return number


# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file.

# The doctests are just examples. Feel free to add your own doctests.

# ****************************************
# Problem 1
# ****************************************
def get_position(ch):
    """
    str -> int
    Return positon of letter in alphabet. If argument is not a letter function
    should return None.

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')

    """
    return ch


# ****************************************
# Problem 2
# ****************************************
def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('C', 'b')
    True
    >>> compare_char('d', 'ad')

    >>> compare_char('2', 2)

    """

    if not isinstance(ch1, str)  or not isinstance(ch2, str)  or len(ch1)*len(ch2) != 1:
        return None

    if 64 < ord(ch1) < 91:
        ch1 = chr((ord(ch1) + 32))
    if 64 < ord(ch2) < 91:
        ch2 = chr((ord(ch2) + 32))

    for i in [ch1, ch2]:
        if ord(i) > 122 or ord(i) < 97:
            return None

    if ord(ch1) > ord(ch2):
        return True

    return False


# ****************************************
# Problem 3
# ****************************************
def compare_str(s1, s2):
    """
    (str, str) -> bool
    Compare two srings lexicographicly. Return True if string s1 is larger
    than string s2 and False otherwise. If arguments aren't string or function
    have different length function should return None.

    >>> compare_str('abc', 'Abd')
    False
    >>> compare_str('zaD', 'zab')
    True
    >>> compare_str('zaD', 'Zad')
    False
    >>> compare_str('aaa', 'aaaaa')

    >>> compare_str('2015', 2015)

    """
    return s2,s1


# ****************************************
# Problem 4
# ****************************************
def type_by_angles(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such angles, then function should return None.

    >>> type_by_angles(60, 60, 60)
    'acute triangle'
    >>> type_by_angles(90, 30, 60)
    'right angled triangle'
    >>> type_by_angles(120, 30, 30)
    'obutuse triangle'
    >>> type_by_angles(100.5, 40, 39.5)
    'obutuse triangle'
    >>> type_by_angles(70, 50.5, 59.5)
    'acute triangle'
    >>> type_by_angles(45.6,44.4,90)
    'right angled triangle'
    >>> type_by_angles(2015, 2015, 2015)

    """
    if a+b+c !=180:
        return None

    biggest_angle=max(a,b,c)

    if biggest_angle>90:
        return "obutuse triangle"
    if biggest_angle==90:
        return "right angled triangle"

    return "acute triangle"




# ****************************************
# Problem 5
# ****************************************
def type_by_sides(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's sides and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such sides, then function should return None.

    >>> type_by_sides(3, 3, 3)
    "acute triangle"
    >>> type_by_sides(3, 4, 5)
    "right angled triangle"
    >>> type_by_sides(3, 3, 2015)
    """
    return a,b,c


# ****************************************
# Problem 6
# ****************************************
def remove_spaces(s):
    """
    str -> str
    Remove all additional spaces in string and return a new string without additional spaces.
    If argument is not a string function should return None.

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    "I'll make him an offer he can't refuse."
    >>> remove_spaces("Great    men     are    not born great, they grow great...")
    'Great men are not born great, they grow great...'
    >>> remove_spaces("     No    matter    how hard  you tried...     ")
    'No matter how hard you tried...'
    >>> remove_spaces("    ")

    >>> remove_spaces("")

    >>> remove_spaces(2015)

    """

    if not isinstance(s, str)  or s==' '*len(s) :
        return None

    output=''
    starting=0
    finish=len(s)-1

    while s[starting]==' ':
        starting+=1

    while s[finish]==' ':
        finish-=1

    for i in range(starting, finish+1):
        if  not s[i]==s[i-1]==' ':
            output+=s[i]

    return output



# ****************************************
# Problem 7
# ****************************************
def convert_to_column(s):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> convert_to_column("Revenge is a dish that tastes best when served cold.")
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> convert_to_column("Never hate your enemies. It affects your judgment.")
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> convert_to_column(2015)
    """

    if not isinstance(s, str):
        return None

    list_of_text = s.split()
    output = []
    i = 0

    for word in list_of_text:
        if word!=' ':
            output.append('')
            for symbol in word:
                if 64 < ord(symbol) < 91:
                    output[i] += symbol.lower()
                elif 96 < ord(symbol) < 123:
                    output[i] += symbol
        i += 1

    return print( '\n'.join(output)+'\n')

# ****************************************
# Problem 9
# ****************************************
def replace_with_stars(s):
    """
    str -> str
    Replace symbols in string with stars. If argument is not a string function should
    return None.

    >>> replace_with_stars("Revenge is a dish that tastes best when served cold.")
    '****************************************************'
    >>> replace_with_stars("Never hate your enemies. It affects your judgment.")
    '**************************************************'
    >>> replace_with_stars('  ')
    '**'
    >>> replace_with_stars('')

    >>> replace_with_stars('2015')
    '****'
    >>> replace_with_stars(2015)

    """

    if not isinstance(s, str) or len(s)==0:
        return None

    return '*'*len(s)


# ****************************************
# Problem 10
# ****************************************
def encrypt_message(s):
    """
    str -> str
    Replace all letters in string with next letters in aplhabet. If argument is not a string
    function should return None.

    >>> encrypt_message("Revenge is a dish that tastes best when served cold.")
    Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.
    >>> encrypt_message("Never hate your enemies. It affects your judgment.")
    Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.
    >>> encrypt_message(2015)

    """
    return s


# ****************************************
# Problem 11
# ****************************************
def decrypt_message(s):
    """
    str -> str
    'Replace all letters in string with previous letters in aplhabet. If argument isn't a string
    function should return None.'

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    'Revenge is a dish that tastes best when served cold.'
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    'Never hate your enemies. It affects your judgment.'
    >>> decrypt_message(2015)

    >>> decrypt_message("Letter a is in this text")
    'Kdssdq z hr hm sghr sdws'
    """
    if not isinstance(s, str) :
        return None

    output=''

    for symbol in s:
        if 91>(ord(symbol))>65 or 123>ord(symbol)>97:
            output+=chr(ord(symbol)-1)
        elif ord(symbol) in  [65, 97]:
            output+=chr(ord(symbol)+25)
        else:
            output+=symbol

    return output


# ****************************************
# Problem 12
# ****************************************
def exclude_letters(s1, s2):
    """
    (str, str) -> str
    Delete all letter from string s2 in string s1. If arguments aren't strings function should
    return None.

    >>> exclude_letters("aaabb", "b")
    aaa
    >>> exclude_letters("abcc", "cczzyy")
    ab
    >>> exclude_letters(2015, "sasd")

    """
    return s1,s2


# ****************************************
# Problem 13
# ****************************************
def create_string(lst):
    """
    list -> str
    Create and return string from histogrma of letters. If argument isn't list of 26 positive
    integer numbers function should return None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0])
    bcc
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,4])
    aaaazzzz
    >>> create_string([4, 0, 0, 0, 0, 0])

    """
    return lst


# ****************************************
# Problem 14
# ****************************************
def get_letters(n):
    """
    int -> str
    Create and return string of first n letters of an alphabet. If arguments isn't
    positive integer number function should return None.

    >>> get_letters(0)

    >>> get_letters(1)
    a
    >>> get_letters(-2015)

    """
    return n


# ****************************************
# Problem 15
# ****************************************
def find_intersection(s1, s2):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    b
    >>> find_intersection("aZAbc", "zzYYxp")
    z
    >>> find_intersection("sfdfsdf", 2015)

    """
    return s1,s2


# ****************************************
# Problem 16
# ****************************************
def find_union(s1, s2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'AYZabcpxz'
    >>> find_union("sfdfsdf", 2015)

    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        return None

    output=''
    for ord_letter in range(65,91):
        letter=chr(ord_letter)
        if letter in s1  or  letter in s2 :
            output+= letter

    for ord_letter in range(97,123):
        letter=chr(ord_letter)
        if letter in s1  or  letter in s2 :
            output+= letter
    return output


# ****************************************
# Problem 17
# ****************************************
def number_of_occurence(lst, s):
    """
    (list, str) -> int
    Find and return number of occurence of string s in all elements of the
    list lst. If lst isn't list of strings or s isn't string function should
    return None.

    >>> number_of_occurence(["man", "girl", "women", "boy"], "m")
    2
    >>> number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba")
    2
    >>> number_of_occurence([1, 2, 2015, 1, 3], "1")

    """
    return lst,s


# ****************************************
# Problem 18
# ****************************************
def number_of_capital_letters(s):
    """
    str -> str
    Find and return number of capital letters in string. If argument isn't string
    function should return None.

    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_capital_letters("EOFError")
    4
    >>> number_of_capital_letters("WHAT IS IT")
    8
    >>> number_of_capital_letters("error")
    0
    >>> number_of_capital_letters(1)

    """
    number=0
    if not isinstance(s, str):
        return None

    for symbol in s:
        if 91>ord(symbol)>64:
            number+=1
    return number


# ****************************************
# Problem 19
# ****************************************
def polygon_area(vertices):
    """
    >>> polygon_area([(4,10), (9,7), (11,2), (2,2)])
    45.5
    >>> polygon_area([(9,7), (11,2), (2,2), (4, 10)])
    45.5
    >>> polygon_area([(0, 0), (0.5,1), (1,0)])
    0.5
    >>> polygon_area([(0, 10), (0.5,11), (1,10)])
    0.5
    >>> polygon_area([(-0.5, 10), (0,-11), (0.5,10)])
    10.5

    """
    return vertices


# ****************************************
# Problem 20
# ****************************************
def polynomial_eval(coefficients, value):
    """
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    >>> polynomial_eval([2,3,0,4], 4)
    180
    # f(x) = 6, f(42) = 6
    >>> polynomial_eval([6], 42)
    6
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """

    return coefficients,value


# ****************************************
# Problem 21
# ****************************************
def polynomials_multiply(polynom1, polynom2):
    """
    (list,list) -> list
    Find and return coeficients of the polynom gotten by the multiplication
    of two  polynoms

    >>> polynomials_multiply([2], [3])
    [6]
    >>> polynomials_multiply([2,-4],[3,5])
    [6, -2, -20]
    >>> polynomials_multiply([2,0,-4],[3,0,2,0])
    [6, 0, -8, 0, -8, 0]

    """
    len_1=len(polynom1)
    len_2=len(polynom2)
    result=[0]*(len_1+ len_2-1)

    for i in range (len_1):
        for j in range (len_2):
            result[i+j] +=polynom1[i]*polynom2[j]

    return result


# ****************************************
# Problem 22
# ****************************************
def pattern_number(sequence):
    """
    >>> pattern_number([])
    None
    >>> pattern_number([42])
    None
    >>> pattern_number([1,2])
    None
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    None
    >>> pattern_number([1,2,3,1,2,3])
    ([1,2,3], 2)
    >>> pattern_number([1,2,3,1,2])
    None
    >>> pattern_number([1,2,3,1,2,3,1])
    None
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    None
    """

    return sequence


# ****************************************
# Problem 23
# ****************************************
def one_swap_sorting(sequence):
    """
    list -> bool
    Return True if sequense is sorted after swapping two elements.
    False in other situations

    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    False
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """

    if len(sequence) < 2:
        return False
    if len(sequence) == 2 and sequence[0] == sequence[1]:
        return False
    wrong_position=0

    for i in range(1,len(sequence)):
        if sequence[i]<sequence[i-1]:
            wrong_position+=1
        if wrong_position > 2:
            return False

    if wrong_position == 0:
        return False

    return True

# ****************************************
# Problem 24
# ****************************************
def numbers_Ulam(n):
    """
    int -> list
    Return sequence of first n Ulam numbers.

    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    >>> numbers_Ulam(25)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97]
     """


    if n==1:
        return [1]
    ulan=[1,2]

    for position in range (2,n):
        temp_list=[0]*(ulan[position-1]+ulan[position-2])

        for i in range(len(ulan)-1):
            for j in range(i+1, len(ulan)):
                if (ulan[i]+ulan[j] )not in ulan:
                    temp_list[ulan[i]+ulan[j]-1]+=1

        ulan.append(temp_list.index(1)+1)

    return ulan


# ****************************************
# Problem 25
# ****************************************
def happy_number(n):
    """
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """

    return n


# ****************************************
# Problem 26
# ****************************************
def sum_of_divisors(n, lst):
    """
    Find and return sum of all odd numbers in the list, that are divisible by n.

    >>> sum_of_divisors(3, [2, 0, 1, 5])
    0
    >>> sum_of_divisors(5, [2, 0, 1, 5])
    5
    >>> sum_of_divisors(7, [])
    0

    """
    return n, lst


# ****************************************
# Problem 27
# ****************************************
def turn_over(n, lst):
    """
    (int, list) -> list
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.

    >>> turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> turn_over(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> turn_over(-5, [])
    []
    """
    if    n<=0:
        return []

    return lst[n-1::-1] + lst [n::1]


# ****************************************
# Problem 28
# ****************************************
def generate_number(number, digit, position):
    """
    Take a number and returns a new one with a digit
    inserted in a given position if digit is bigger
    then initital digit in position

    >>> generate_number(3746, 5, 0)
    3746
    >>> generate_number(3746, 5, 1)
    3756
    >>> generate_number(3746, 5, 2)
    3746
    >>> generate_number(3746, 5, 3)
    5746
    >>> generate_number(3746, 5, 4)
    53746
    >>> generate_number(3746, 5, 7)
    50003746
    >>> generate_number(-12345, 9, 10)
    -90000012345
    """
    return number,digit,position

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
