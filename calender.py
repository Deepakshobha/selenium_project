from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import re
import csv
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get(r"https://www.goibibo.com/")
driver.find_element_by_xpath("//span[text()='Departure']").click()
# driver.find_element_by_xpath("//div[text()='May 2022']/../..//p[text()='26']").click()


month = 'July 2022'
day = '25'
for _ in range(12):
    try:
        driver.find_element_by_xpath(f"//div[text()='{month}']/../..//p[text()='{day}']").click()
        break
    except NoSuchElementException:
        driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
        sleep(1)
        continue