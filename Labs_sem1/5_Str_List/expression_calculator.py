def calculate_expression(expression):
    """
    Return result of the calculation in text of the expression (by its description beyong
    standart : ['додати', 'плюс','мінус','відняти','помножити на','поділити на'])
    Ignore opperation priority if not return 'Неправильний вираз!'.
    Prediction: opperations in expression are in standart opperation list
    >>> calculate_expression("Скільки буде 5 додати 5?")
    10
    >>> calculate_expression("Скільки буде 2 додати 10 помножити на 7?")
    84
    >>> calculate_expression("Скільки буде 2 2 додати?")
    'Неправильний вираз!'
    >>> calculate_expression("Скільки сезонів в році?")
    'Неправильний вираз!'
    """
    standart_operations = ['додати', 'плюс','мінус','відняти','помножити на','поділити на']
    text_lenght= len(expression)
    expression_numbers = []   # list of numbers in expression
    expression_operations = [] # list of operations in expression

    i = 0
    while i < text_lenght:  # find oppperations and numbers in expression add them to lists

        for operation in standart_operations: # find operations in text
            oper_l = len(operation)
            # check if text started from i symbol is in standart operations
            if expression[i : (i + oper_l) % text_lenght] == operation:
                # add operation with it starting symbol index
                # to the list of operations in an expression
                expression_operations.append([operation, i])
                i += oper_l

        if expression[i].isnumeric():  # find numbers in text
            #check if the number is negative if yes add '-' before it
            if expression[i-1] == '-':
                expression_numbers.append([expression[i-1], i])
                expression_numbers[-1][0] += expression[i]
            else:
                # add it and its text index to a new list element
                expression_numbers.append([expression[i], i])
            # determine a full number with all digits
            while  i < text_lenght - 1 and expression[i+1].isnumeric()  :
                i+=1
                expression_numbers[-1][0] += expression[i]
            expression_numbers[-1][0] = int(expression_numbers[-1][0])

        i += 1

    len_numbers = len(expression_numbers)
    len_operations = len(expression_operations)
    if len_numbers != len_operations + 1 or len_operations == 0:
        return 'Неправильний вираз!'

    while len_numbers > 1:
        # check if there is an operation between two consistest numbers in expression
        if expression_numbers[0][1] < expression_operations[0][1] < expression_numbers[1][1]:

            # calculate result of the operation base on its type
            if expression_operations[0][0] in ['додати', 'плюс']:
                operation_result = expression_numbers[0][0] + expression_numbers[1][0]
            elif expression_operations[0][0] in ['відняти', 'мінус']:
                operation_result = expression_numbers[0][0] - expression_numbers[1][0]
            elif expression_operations[0][0] == 'помножити на':
                operation_result = expression_numbers[0][0] * expression_numbers[1][0]
            elif expression_numbers[1][0] != 0:
                operation_result = expression_numbers[0][0] / expression_numbers[1][0]
            else:
                return 'Неправильний вираз!'

            expression_numbers[1][0] = operation_result
            expression_numbers.pop(0)
            expression_operations.pop(0)

        else:
            return 'Неправильний вираз!'

        len_numbers -=1

    return expression_numbers[0][0]
