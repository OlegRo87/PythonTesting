# implicit wait global wait
# explicit wait
# pause(time.sleep)
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/')
driver.find_element_by_css_selector('input.search-keyword').send_keys("ber")
time.sleep(4)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
driver.find_element_by_class_name('promoBtn').click()
print(driver.find_element_by_css_selector('span.promoInfo').text)