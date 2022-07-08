import calendar

def semester_calendar(output_type, year, first_month, last_month):
    """
    Return calendar by year and monthes
    >>> print(semester_calendar("txt", 2016, 2, 3))
       February 2016
    Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29
         March 2016
    Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6
     7  8  9 10 11 12 13
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28 29 30 31
    """

    output = ''
    cal = calendar.HTMLCalendar(calendar.MONDAY)
    for current_month in range(first_month, last_month + 1):
        output += cal.formatmonth(year, current_month)
    if output_type == 'html':
        return output[:-1]

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthes = ['', 'January', 'February', '  March', 'April', 'Mai', 'June', 'Jule',
               'August', 'September', 'October', 'November', 'December']

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29

    first_day_in_year = (6 + (year - 2022) - (abs(2024 - year)) // 4
                         + (abs(2100 - year)) // 100 - (abs(2400 - year)) // 400) % 7

    result = ''
    for current_month in range(first_month, last_month + 1):
        first_day_in_month = (first_day_in_year - 1 +
                              sum(days_in_month[:current_month])) % 7 + 1
        result += (f'   {monthes[current_month]} {year}\nMo Tu We Th Fr Sa Su\n')
        result += ' ' * 3 * (first_day_in_month - 1)
        day_number = 1

        while day_number <= 8 - first_day_in_month:
            result += f' {day_number} '
            day_number += 1

        result = result[: -1] + '\n'
        new_line_check = 1

        while day_number <= days_in_month[current_month]:
            if day_number < 10:
                result += ' '
            result += f'{day_number} '

            if new_line_check % 7 == 0:
                result = result[: -1] + '\n'
            new_line_check += 1
            day_number += 1

        result = result[: -1] + '\n'

    if output_type == 'txt':
        return result[: -1]


print(semester_calendar('txt', 2016, 2, 3))
