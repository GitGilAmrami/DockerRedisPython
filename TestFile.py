#  import selenium

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\gilam\\Desktop\\DevOps\\ChromeDriver.exe")
### Enter the Site
driver.get("http://192.168.99.100:7000/")
driver.implicitly_wait(10)

/html