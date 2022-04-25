from selenium.webdriver import Chrome
from time import sleep
import csv
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
# driver.get("file:///C:/Users/Deepak%20M/Desktop/selenium/demo-html/demo.html")
# driver.find_element_by_xpath("//td[text()='Python']/..//input[@type='checkbox']").click() #search for the name and click
# driver.get("file:///C:/Users/Deepak%20M/Desktop/selenium/demo-html/demo.html")


# driver.get("https://www.python.org/downloads/")
# driver.find_element_by_xpath("//a[text()='Python 3.9.10']/../..//a[text()='Release Notes']").click()


# driver.get("http://demowebshop.tricentis.com/books")
# driver.find_element_by_xpath("//a[text()='Fiction']/../..//input[@value='Add to cart']").click()


# driver.get("http://demowebshop.tricentis.com/desktops")
# ele=driver.find_element_by_xpath("//a[text()='Build your own cheap computer']/../..//span[@class='price actual-price']")
# print(ele.text)

#
# driver.get("http://demowebshop.tricentis.com/books")
# eles=driver.find_elements_by_xpath("//div[@class='product-grid']//a")
# for ele in eles:
#     print(ele.text)



# driver.get("http://demowebshop.tricentis.com/books")
# eles=driver.find_elements_by_xpath("//span[@class='price actual-price']")
# for ele in eles:
#     print(ele.text)

with open(r"C:\Users\Deepak M\Desktop\pythonProject2\selenium_project\sam.csv")as f:
    rows = csv.reader(f)
    headers=next(rows)
    expected = {row[0]:float(row[1]) for row in rows}
print(expected)