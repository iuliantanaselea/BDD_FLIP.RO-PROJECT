Feature: filters feature

  Background:
    Given I am on the "https://flip.ro/" page

  @filters
  Scenario Outline: Verify category filter
    When I enter "<brand>" on the search bar
    And I click on the search button
    And I click on the "<filter>" checkbox
    Then I should have a list of "<model>" products
    Examples:
      | brand | filter    | model  |
      | Apple | Tablete   | iPad   |
      | Apple | Telefoane | iPhone |

  @filters
  Scenario Outline: Verify price filter
    When I enter "Apple" on the search bar
    And I click on the search button
    And I click on the "<range>" radio button
    Then I should have a list of products between "<range>" price
    Examples:
      | range     |
      | 500-1.000 |

  @filters_2
  Scenario Outline: Verify product condition filter
    When I enter "<brand>" on the search bar
    And I click on the search button
    And I click on the "<conditie>" checkbox
    Then I should have a list of products with the condition described as "<conditie>"
    Examples:
      | brand | conditie      |
      | Apple | Ca nou        |
      | Apple | Excelent      |
      | Apple | Foarte bun    |
      | Apple | Bun           |
      | Samsung | Bun         |





