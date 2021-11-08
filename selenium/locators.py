import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element_by_name("name").send_keys("oleg")
driver.find_element_by_name("email").send_keys("oleg@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys('123456')
driver.find_element_by_name("name").clear()
driver.find_element_by_name("name").send_keys("oleg")
driver.find_element_by_id("exampleCheck1").click()

# select class dropdown menu
dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
dropdown.select_by_index(0)  # will choose male


driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/input").click()
message = driver.find_element_by_class_name("alert-success").text

# print(driver.find_element_by_css_selector("body > app-root > form-comp > div > form > div:nth-child(1) > label").text)
# print(driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[2]/label").text)

# driver.find_element_by_link_text('Shop').click()

assert "success" in message
