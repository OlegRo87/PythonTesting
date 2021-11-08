import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))
#
# for checkbox in checkboxes:
#     checkbox.click()
#     assert checkbox.is_selected()  # if all checkboxes are selected


# click on one of options

for checkbox in checkboxes:
    print(checkbox.get_attribute('value'))
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()  # if all checkboxes are selected

radio_buttons = driver.find_elements_by_xpath("//input[@type='radio']")
radio_buttons[2].click()
assert radio_buttons[2].is_selected()

