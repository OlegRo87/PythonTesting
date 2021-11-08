import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

validate_text = "Option3"
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# first case


driver.find_element_by_id('name').send_keys(validate_text)
driver.find_element_by_id('alertbtn').click()

# grab popup window(not html)
alert = driver.switch_to.alert
alert_text = alert.text
assert validate_text in alert_text
alert.accept()  # agree/yes/ok

# second case


driver.find_element_by_id('name').send_keys(validate_text)
driver.find_element_by_id('confirmbtn').click()
# grab popup window(not html)
alert = driver.switch_to.alert
alert.dismiss()  # cancel
