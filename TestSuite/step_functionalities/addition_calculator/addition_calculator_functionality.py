from TestSuite.constants.addition_calculator import addition_calculator_constants as const
from TestSuite.reusable_functionalities.re_usable_function import addition_of_numbers
def read_data_from_constants(context):
    context.f_num = const.first_number
    context.s_num = const.second_number
    context.t_num = const.third_number

def read_data_from_input_excel(context):
    pass


def performing_addition_operation(context):
    number_list = [context.f_num, context.s_num, context.t_num]
    context.result = addition_of_numbers(number_list)

def showcase_generated_results(context):
    print(f"The sum of '{context.f_num, context.s_num, context.t_num}' is = {context.result}")