Feature: # Test for Amazon Sign in

  Scenario: #Verify that logged out user sees Sign In when clicking on Returns and Orders
    Given Open amazon page
    When Click on Returns and Orders button
    Then Sign in page shows