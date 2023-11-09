Feature: search feature

  Background:
    Given I am on the https://flip.ro/ page

  Scenario: Search Samsung products
    When I enter "Samsung" on the search bar
    And I click on the search button
#    Then I should see "Samsung" as filter
    Then I should have a list of "Samsung" products

#  Scenario: Search Apple products
#    When I enter "Apple" on the search bar
#    And I click on the search button
#    Then I should see "Apple" as filter
#    And I should have a list of "Apple" products
#
#  Scenario: Search Huawei products
#    When I enter "Huawei" on the search bar
#    And I click on the search button
#    Then I should see "Huawei" as filter
#    And I should have a list of "Huawei" products
#
#  Scenario: Search Xiaomi products
#    When I enter "Xiaomi" on the search bar
#    And I click on the search button
#    Then I should see "Xiaomi" as filter
#    And I should have a list of "Xiaomi" products