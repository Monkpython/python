from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://youtube.com')

link = driver.find_element_by_partial_link_text("Trending")
link.click()

time.sleep(10)

link = driver.find_element_by_partial_link_text("Home")
link.click()

time.sleep(5)

driver.quit()