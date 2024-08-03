from behave import given, when, then
from git.TestSuite.step_functionalities.addition_calaulator.addition_calculator_functionality import \
    read_data_from_input_excel

@given("fetch the numbers from constant file")
def step_impl(context):
    read_data_from_input_excel(context)


@when("perform the addition operation")
def step_impl(context):
    performing_addition_operation(context)


@then("generate the results")
def step_impl(context):
    showcase_generated_results(context)


@given("fetch the numbers from input excel where f_num is {f_num_format} and s_num is {s_num_format}")
def step_impl(context, f_num_format, s_num_format):
    pass


@then("upload the result file")
def step_impl(context):
    pass
