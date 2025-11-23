from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

#select Webdriver.
driver = webdriver.Chrome() #-- I am using Chrome as my webdriver. 

#Trying with python
driver.get("http://www.python.org")

assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")  # -- Gave input to search pycon on the python website.
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source  # -- If no valid results found then display message as No results found. 
time.sleep(10) # -- Set a timer so that I can view my results. If not given a timer then the code will execute and provide results within a second (which would be difficult to view the results)
driver.close()