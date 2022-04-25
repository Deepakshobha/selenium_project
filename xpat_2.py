#
driver.get(r"http://demowebshop.tricentis.com/desktops")
# driver.find_element_by_xpath("//td[text()='Python']/..//input[@name='download']").click()
# driver.find_element_by_xpath("//a[text()='Python 3.9.10']/../..//a[text()='Release Notes']").click()
# price_tag = driver.find_element_by_xpath("//span[@class='price actual-price'][1]").text
# print(price_tag)
# price_tag = driver.find_element_by_xpath("//a[text()='Elite Desktop PC']/../..//span[@class='price actual-price']").text
# print(price_tag)
#
#
# expected_prices = {'Elite Desktop PC':1350.00,'Simple Computer':800.00,'Build your own computer':180.00}
# for product,expected_price in expected_prices.items():
#     price_tag = driver.find_element_by_xpath(f"//a[text()='{product}']/../..//span[@class='price actual-price']").text
#     if expected_price==float(price_tag):
#         print("pass")
#     else:
#         print(f'expected_price is {product} is  {expected_price}but actual_price is{price_tag}')


with open(r"C:\Users\Deepak M\Desktop\pythonProject2\selenium_project\sample.csv") as f:
    rows = csv.reader(f)
    header = next(rows)
    expected_price = {row[0]:float(row[1]) for row in rows}
print(expected_price)

#
# driver.find_element_by_xpath("//a[text()='Simple Computer']/../..//input[@value='Add to cart']").click()