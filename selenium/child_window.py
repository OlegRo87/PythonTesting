from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element_by_link_text('Click Here').click()
child_window = driver.window_handles[1]  # extract list of windows that opened by automation("parentid", "childid")
driver.switch_to.window(child_window)
print(driver.find_element_by_tag_name("h3").text)
driver.close()  # will close only exact window
driver.switch_to.window(driver.window_handles[0])

assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
