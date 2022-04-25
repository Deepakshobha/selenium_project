from selenium.webdriver import Chrome
from time import sleep
import csv
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get("http://demowebshop.tricentis.com")

#left navigation
# links=driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
#
# for link in links:
#     print(link.text)

#footer
links=driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']")

for link in links:
    print(link.text)

