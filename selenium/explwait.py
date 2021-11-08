# implicit wait global wait
# explicit wait local to specific chank of code(line)
# pause(time.sleep)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
list_1 = []
list_2 = []
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/')
driver.find_element_by_css_selector('input.search-keyword').send_keys("ber")
time.sleep(4)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# //div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons:
    list_1.append(button.find_element_by_xpath('parent::div/parent::div/h4').text)
    button.click()
print(list_1)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'promoCode')))

veg = driver.find_elements_by_css_selector("p.product-name")
for product in veg:
    list_2.append(product.text)
print(list_2)
assert list_1 == list_2
orig_amount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
driver.find_element_by_class_name('promoBtn').click()
time.sleep(5)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
disc_amount = driver.find_element_by_css_selector(".discountAmt").text
assert float(disc_amount) < int(orig_amount)
print(driver.find_element_by_css_selector('span.promoInfo').text)

amounts = driver.find_elements_by_xpath("//tr//td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)  # 48 + 160 + 180
print(sum)
total_amount = int(driver.find_element_by_class_name("totAmt").text)
assert total_amount == sum