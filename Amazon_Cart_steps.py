from selenium.webdriver.common.by import By
from behave import given, when, then


@then('The Amazon Cart is empty')
def cart_is_empty(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(),'Your Amazon Cart is empty')]").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got {actual_result}.'


@then('The Amazon Cart has the "Yankee Candle Vanilla Cupcake Scented" in quantity "2"')
def cart_has_product(context):
    expected_result = "Yankee Candle Vanilla Cupcake Scented"
    assert context.driver.find_element(By.XPATH, "//*[@id='activeCartViewForm']//img[contains(@alt,'Yankee Candle Vanilla Cupcake Scented')]").is_displayed(), f'Error! The cart does not have the {expected_result}.'
    assert "2" == context.driver.find_element(By.XPATH, "//*[@id='activeCartViewForm']//*[@id='a-autoid-5-announce']/span[2]").text, f'Error! Wrong quantity.'

