
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# Mac OS X PATH
driver = webdriver.Chrome('/Users/sayem/Dropbox/ChromeDriver/chromedriver')

# Windows PATH
#driver = webdriver.Chrome('C:\Users\Administrator\Dropbox\ChromeDriver\cchromedriver.exe')

# Go to URL
driver.get("http://www.totsy.com")

# Implicit wait time
driver.implicitly_wait(30)

# Login Credentials
driver.find_element_by_css_selector("#email").send_keys("ssayem+l9@totsy.com")
driver.find_element_by_css_selector("#pass").send_keys("user123")
driver.find_element_by_css_selector("#submit-button").click()

# Mouse hover to SHOP BY CATEGORY
shop_by_age = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_age)
hover.perform()

# Click on Shoes
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[4]/a").click()

# Close Browser
driver.close()
