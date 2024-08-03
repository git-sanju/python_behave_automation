from behave import given, when, then
from TestSuite.step_functionalities.addition_calculator.addition_calculator_functionality import \
    read_data_from_constants,performing_addition_operation,showcase_generated_results

@given("fetch the numbers from constant file")
def step_impl(context):
    read_data_from_constants(context)


@when("perform the addition operation")
def step_impl(context):
    performing_addition_operation(context)


@then("generate the results")
def step_impl(context):
    showcase_generated_results(context)


@given("fetch the numbers from input excel where f_num is {f_num_format} and s_num is {s_num_format}")
def step_impl(context, f_num_format, s_num_format):
    read_data_from_input_excel(context)


@then("upload the result file")
def step_impl(context):
    pass
