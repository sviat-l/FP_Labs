"""
Gef file by its url
Create list of string
Create CSV file with that date
"""
import urllib.request

def read_input_file(url: str, number: int) :
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',2)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',0)
    []
    """
    list_of_url_date = []
    # read lines from  file
    with urllib.request.urlopen(url) as web_page :
        max_number_of_lines_to_read = number * 8
        number_of_read_lines = 0
        for line in web_page:
            number_of_read_lines += 1
            list_of_url_date.append(line.strip().decode('utf-8'))
            if number_of_read_lines == max_number_of_lines_to_read:
                break
    print(list_of_url_date)

    number_of_students_added = 0
    num_line = 2
    list_of_student = []

    while number_of_students_added < number:
        if list_of_url_date[num_line][0].isnumeric():
            current_line = list_of_url_date[num_line].split()
            atestat = float(list_of_url_date[num_line+3][-5:])
            atestat = [str(atestat)+'0']
            # atestat = [str({{:.4f}.format(float(list_of_url_date[num_line+3][-5:]):4})))]
            student_name = [' '.join(current_line[1:4])]
            points  = [current_line[6]]
            # cur_num = [current_line[0]]
            cur_num = [str(number_of_students_added+1)]
            accept = ['+']
            # if current_line[4] != 'До':
            #     accept = ['-']

            list_of_student.append(cur_num + student_name + accept + points + atestat)
            number_of_students_added += 1
            num_line += 6
        num_line += 1

    return list_of_student


def write_csv_file(url: str):
    """
    Write CSV file from url
    """
    csv_list =read_input_file(url,77)
    with open ('total.csv', 'w', encoding='utf-8') as output_file:
        output_file.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
        for line in csv_list:
            output_file.write(','.join(line)+'\n')

write_csv_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt')
# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())


print(read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',2))