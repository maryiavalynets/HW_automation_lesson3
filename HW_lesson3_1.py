from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/')

#Logo Amazon
driver.find_element(By.CSS_SELECTOR,".a-icon.a-icon-logo")
#Create account
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")
#"Your name" input field
driver.find_element(By.CSS_SELECTOR,"#ap_customer_name")
#"Mobile number or email" input field
driver.find_element(By.CSS_SELECTOR,"#ap_email")
#"Password" input field
driver.find_element(By.CSS_SELECTOR,"#ap_password")
#"Re-enter password" input field
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")
#Text "Passwords must be at least 6 characters"
driver.find_element(By.XPATH,"//*[contains(text(),'Passwords must be at least 6 characters.')]")
#"Continue" button
driver.find_element(By.CSS_SELECTOR,"#continue")
#Link "Conditions of Use"
driver.find_element(By.CSS_SELECTOR,"div#legalTextRow a[href*=ap_register_notification_condition_of_use]")
#Link "Privacy Notice"
driver.find_element(By.CSS_SELECTOR,"div#legalTextRow a[href*=ap_register_notification_privacy_notice]")
#Link "Sign in"
driver.find_element(By.CSS_SELECTOR,"a.a-link-emphasis")


