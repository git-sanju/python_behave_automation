@addition_cal
Feature: Performing addtion operation

  @add_three_num
  Scenario: Addition of the three numbers
    Given fetch the numbers from constant file
    When perform the addition operation
    Then generate the results

#  @add_two_num
#  Scenario Outline: Performing addition operation on two numbers
#    Given fetch the numbers from input excel where f_num is <first_number_format> and s_num is <second_number_format>
#    When perform the addition operation
#    Then generate the results
#    And upload the result file
#    Examples:
#      | first_number_format | second_number_format |
#      | positive            | positive             |
#      | positive            | negative             |
#      | negative            | positive             |
#      | negative            | negative             |