from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys('hello')
print(driver.find_element_by_name("name").text)  # no print
print(driver.find_element_by_name("name").get_attribute("value"))
# now we can give js pure command
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shop_button = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shop_button)  # java script code
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")  # scroll on page
