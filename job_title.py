from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from time import sleep
import csv

driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get(r"https://www.monsterindia.com/search/python-jobs?searchId=86b497ff-a319-4e1f-acb2-16d20dcc188c")
links=driver.find_elements_by_xpath("//div[@class='job-tittle']")
for link in links:
    print(link.text)

