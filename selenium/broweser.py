from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Firefox()
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get('https://google.com')

print(driver.title)
print(driver.current_url)
driver.get('https://google.com/maps/')
driver.minimize_window()
driver.back()
driver.refresh()

driver.close()  # only current window will close
# driver.quit()  # all windows will close
