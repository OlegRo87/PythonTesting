import time
from selenium import webdriver


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")  # common selector to all countries
# after input start name
print(len(countries))  # total num of countries that started on "ind"
for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"  # more generic than previous
