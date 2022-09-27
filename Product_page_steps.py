from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on the quantity icon')
def click_on_quantity_icon(context):
  context.driver.find_element(By.ID, 'a-autoid-0-announce').click()


@when('Click on the number "2" from the quantity values')
def click_on_quantity_icon(context):
  context.driver.find_element(By.ID, 'quantity_1').click()


@when('Click on the "Add to Cart" button')
def click_on_quantity_icon(context):
  context.driver.find_element(By.ID, 'add-to-cart-button').click()


@when('Click on the "Cart" button')
def click_on_cart_button(context):
  cart_button = context.driver.find_element(By.ID,'attach-view-cart-button-form')
  cart_button.click()