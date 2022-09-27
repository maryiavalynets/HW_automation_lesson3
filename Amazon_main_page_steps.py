from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Returns and Orders button')
def click_on_returns_orders(context):
    context.driver.find_element(By.ID,'nav-orders').click()


@when('Click on the cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.ID,'nav-cart').click()


@when('Input "Yankee Candle Vanilla Cupcake Scented, Classic 22oz Large Jar" into Amazon search field')
def input_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Yankee Candle Vanilla Cupcake Scented, Classic 22oz Large Jar')


@when('Click on the search icon')
def click_on_search_icon(context):
    context.driver.find_element(By.ID,'nav-search-submit-button').click()