from selenium.webdriver import Chrome
from time import sleep
import csv
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get(r"https://www.ajio.com/")
# driver.get(r"https://www.python.org/downloads/")

# with open(r"C:\Users\Deepak M\Desktop\pythonProject2\selenium_project\sample.csv") as f:
#     rows = csv.reader(f)
#     header = next(rows)
#     expected_price = {row[0]:float(row[1]) for row in rows}
# print(expected_price)

element = driver.find_element_by_xpath("//input[@placeholder='Search AJIO']").send_keys("shoes")
ele=driver.find_element_by_xpath("//span[@class='ic-search']").click()
elements=driver.find_elements_by_xpath("//div[@class='ReactVirtualized__Grid__innerScrollContainer']")
for ele in elements:
    print()



#number of items and price
from selenium.webdriver import Chrome
from time import sleep
import re
import csv
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")
eles=driver.find_elements_by_xpath("//h3[@class='art-name']/a/span")
price = driver.find_elements_by_xpath("//span[@class='art-price' or @class='art-price art-price--offer']")

elements=[ele.text for ele in eles]
prices=[eles.text for eles in price]

print(elements,prices)
all_prices=[]
for price in prices:
    actual=float("".join(re.findall(r"[\d\.]",price)))
    all_prices.append(actual)
print(all_prices)

actual_prices={}
for product,price in zip(elements,all_prices):
    actual_prices[product] = price
print(actual_prices)

less_100={product:price for product,price in actual_prices.items() if price<100}
print(less_100)