def addition_of_numbers(number_list):
    '''
    accepts list of numbers perform addition opertion
    :param number_list:
    :return: sum of the numbers in list
    '''
    sum = 0
    if number_list:
        for item in number_list:
            sum = sum + item
    return sum