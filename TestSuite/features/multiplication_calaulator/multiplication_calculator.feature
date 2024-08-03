@multiplication_cal
Feature: Performing addtion operation

  Scenario Outline: Performing multiplication of two given numbers
    Given fetch the numbers from input file
    When perform the addition operation
    Then generate the results
    And generate the file
    Examples:
      | first_number_format | second_number_format |
      | positive            | positive             |
      | positive            | negative             |
      | negative            | positive             |
      | negative            | negative             |


  Scenario: Addition of the three numbers
    Given fetch the numbers from constant file
    When perform the addition operation
    Then generate the results
    And generate the file