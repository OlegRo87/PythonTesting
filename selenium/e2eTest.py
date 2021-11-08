from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector('a[href*="shop"]').click()
products = driver.find_elements_by_xpath('//div[@class="card h-100"]')

# //div[@class="card h-100"]/div/h4/a
# product =  '//div[@class="card h-100"]'

for product in products:
    prod_name = product.find_element_by_xpath('div/h4/a').text  # product + addition...
    if prod_name == "Blackberry":
        # //div[@class="card h-100"]/div/button
        product.find_element_by_xpath('div/button').click()
driver.find_element_by_css_selector('a[class*="btn-primary"]').click()
driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
driver.find_element_by_id('country').send_keys('rus')
wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Russia")))
driver.find_element_by_link_text("Russia").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
success_text = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in success_text

driver.get_screenshot_as_file('screen.png')
