from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Product results for "Yankee Candle Vanilla Cupcake Scented, Classic 22oz Large Jar" are show')
def product_results_are_show(context):
    expected_result = '"Yankee Candle Vanilla Cupcake Scented, Classic 22oz Large Jar"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'


@when('Click on the product icon "Yankee Candle Vanilla Cupcake Scented, Classic 22oz Large Jar"')
def click_on_the_product_icon(context):
    product_icon = context.driver.find_element(By.CSS_SELECTOR, "[href*='Yankee-Candle-Large-Vanilla-Cupcake']")
    product_icon.click()