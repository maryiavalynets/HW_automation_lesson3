
Feature: # Test for Amazon Cart

  Scenario: # Verify that the Amazon Cart is empty when clicking on the cart icon
    Given Open amazon page
    When Click on the cart icon
    Then The Amazon Cart is empty

  Scenario: # Verify that the Amazon Card has the item when adding it into the cart
    # (and check for the number of items in the cart)
    Given Open amazon page
    When Input "Yankee Candle Vanilla Cupcake Scented, Classic 22oz Large Jar" into Amazon search field
    When Click on the search icon
    Then Product results for "Yankee Candle Vanilla Cupcake Scented, Classic 22oz Large Jar" are show
    When Click on the product icon "Yankee Candle Vanilla Cupcake Scented, Classic 22oz Large Jar"
    When Click on the quantity icon
    When Click on the number "2" from the quantity values
    When Click on the "Add to Cart" button
    When Click on the "Cart" button
    Then The Amazon Cart has the "Yankee Candle Vanilla Cupcake Scented" in quantity "2"