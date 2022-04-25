from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from time import sleep
import csv

driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")

# driver.get(r"https://www.ajio.com/s/footwear-4063-31521?query=:relevance")
# element = driver.find_element_by_xpath("//input[@placeholder='Search AJIO']").send_keys("shoes")
# ele=driver.find_element_by_xpath("//span[@class='ic-search']").click()
# driver.find_element_by_xpath("//span[text()='price']").click()
# driver.find_element_by_xpath("//label[@class ='facet-linkname facet-linkname-pricerange facet-linkname-Rs.500-1000']").click()
driver.get("http://demowebshop.tricentis.com/books")

# driver.find_element_by_xpath("//span[@class='ic-search']").click()
shoes_ = driver.find_elements_by_xpath("//span[@class='price actual-price' or @class='price old-price' ]/../../..//a[text()='Computing and Internet']")
for item in shoes_:
    print(item.text)
