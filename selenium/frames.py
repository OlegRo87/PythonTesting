from selenium import webdriver

# iframe, frameset, frame one of those declare there is a frame
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/iframe')
driver.switch_to.frame("mce_0_ifr")  # id of frame, name of frame, index value
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
