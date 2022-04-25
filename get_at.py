# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
# # driver.get("file:///C:/Users/Deepak%20M/Desktop/selenium/demo-html/demo.html")
driver.get("http://demowebshop.tricentis.com/login")
# links = driver.find_elements_by_xpath("//a")
# for link in links:
#     print(link.text,'------>',link.get_attribute("href"))
#     sleep(1)


element=driver.find_element_by_class_name("ico-register")

# print(element.get_attribute("type"))
# print(element.get_attribute("class"))
# print(element.get_attribute("id"))
# print(element.get_attribute("name"))
# #
#
attributes = ["href","class"]

for attribute in attributes:
    print(element.get_attribute(attribute))
#
#
# images = driver.find_element_by_xpath("//img")
# for image in images:
