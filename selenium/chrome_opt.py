from selenium import webdriver

# chrome options
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("--start-maximized")
chrome_opt.add_argument("headless")
chrome_opt.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_opt)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
