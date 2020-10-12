
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

targeturl = "xxxx"
def function1(targeturl):
    driver.get(targeturl)

print('Whats is the Website?'  )
webpage = input()
function1(webpage)

search = driver.find_element_by_name("q")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()