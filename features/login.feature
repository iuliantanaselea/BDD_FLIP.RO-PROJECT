Feature: login feature

  Background:
    Given I am on the "https://flip.ro/autentifica-te/" page

  @login
  Scenario: Login with invalid credentials
    When I enter an incorrect email
    And I enter an incorrect password
    And I click Acceseaza cont button
    Then I should see an error message "Aceasta adresa de e-mail nu este asociata cu un cont existent"
