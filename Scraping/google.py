from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get('http://www.google.com')


search = driver.find_element_by_name('q')
search.send_keys('oh yeah')
search.send_keys(Keys.RETURN)



link = driver.find_element_by_partial_link_text("Yello - Oh Yeah (Official Video")
link.click()

time.sleep(10)

