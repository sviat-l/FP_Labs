"""
Calendar transformation
"""
import calendar as calndar

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekday_name(3)
    'thu'
    """
    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return weekdays[number]


def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message
    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    try:
        day,month_new,year_n = date.split('.')
        day,month_new,year_n = int(day), int(month_new), int(year_n)

        if month_new not in range(1,13):
            raise AssertionError ("month out of range")
        days_in_month = [28,31,29,31,30,31,30,31,31,30,31,30,31]
        if day >  days_in_month[month_new] or day < 1:
            raise AssertionError ("number of days out of range")
        if month_new == 2:
            if year_n % 4 != 0 or (year_n%100 == 0 and year_n%400 != 0):
                if day == 29:
                    raise AssertionError ("number of days out of range")
        calndar.weekday(year_n, month_new, day)
    except ValueError as error:
        raise AssertionError from error

    if month_new <3:
        year_n = year_n -1

    cent, decades = year_n // 100, year_n % 100
    month_1 = ((month_new-3)%12 + 3)
    int_day = (day + (13*(month_1+1))//5 + decades + decades//4 +  cent//4 - 2 * cent + 5 ) % 7
    return int_day

print(weekday(('1.01.2000')))

def calendar(month: int, year: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    output_calendar = ''
    for i  in range(7):
        output_calendar += f'{weekday_name(i)} '

    first_month_day = weekday(f'1.{month}.{year}')
    if month == 2:
        if year % 4 == 0 and (year % 100 !=0  or year % 400 == 0):
            last_day = 29
        else:
            last_day = 28
    elif month in [1,3,5,7,8,10,12]:
        last_day = 31
    else:
        last_day = 30

    list_of_days= first_month_day*[' '] +  list(range(1,last_day+1))
    current_day = 0
    while current_day< len(list_of_days):
        if (current_day)%7==0:
            output_calendar = output_calendar[:-1] +'\n'
        output_calendar += f"{(list_of_days[current_day]):3} "
        current_day += 1

    return output_calendar[:-1]

def transform_calendar(calendar_hor: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    lines_calendar = calendar_hor.split('\n')
    transformed_calendar = [[],[],[],[],[],[],[]]
    num_of_lines = len(lines_calendar)
    for i in range(num_of_lines):
        lines_calendar[i] = (' '.join(lines_calendar[i].split())).split()
        if i==1:
            lines_calendar[1] = [' ']*(7 - len(lines_calendar[1])) + lines_calendar[1]
        j  =  0
        while j <  len(lines_calendar[i]):
            transformed_calendar[j].append(lines_calendar[i][j])
            j += 1
    string_transformed = ''
    for line_transformed in transformed_calendar:
        string_transformed += (' '.join(line_transformed) + '\n')
    return string_transformed[:-1]

import doctest
print(doctest.testmod())

# if __name__ == '__main__':
#     try:
#         print("Type month")
#         month_n = input()
#         month_n = int(month_n)
#         print("Type year")
#         year_new = input()
#         year_new = int(year_new)
#         print("\n\nThe calendar is: ")
#         print (calendar(month_n, year_new))
#     except ValueError as err:
#         print(err)
