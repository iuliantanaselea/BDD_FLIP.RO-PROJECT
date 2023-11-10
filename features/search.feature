Feature: search feature

  Background:
    Given I am on the https://flip.ro/ page

  @search
  Scenario: Search Samsung products
    When I enter "Samsung" on the search bar
    And I click on the search button
    Then I should have a list of "Samsung" products

  @search
  Scenario: Search Apple products
    When I enter "Apple" on the search bar
    And I click on the search button
    Then I should have a list of "Apple" products

  @search
  Scenario: Search Huawei products
    When I enter "Huawei" on the search bar
    And I click on the search button
    Then I should have a list of "Huawei" products

  @search
  Scenario: Search Xiaomi products
    When I enter "Xiaomi" on the search bar
    And I click on the search button
    Then I should have a list of "Xiaomi" products