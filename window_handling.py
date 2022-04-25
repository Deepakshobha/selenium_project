from selenium.webdriver import Chrome
from time import sleep
import re
import csv
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get(r"http://demowebshop.tricentis.com")
# driver.find_element_by_xpath("//a[text()='Twitter']").click()
#
# handles =driver.window_handles
#
#
# driver.switch_to.window(handles[1])
# sleep(1)
#
# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("Hello")
#
# driver.switch_to.window(handles[0])
# sleep(1)

# driver.find_element_by_xpath("//a[text()='Register']").click()


driver.find_element_by_xpath("//input[@value='Search']").click()
# driver.switch_to.alert.accept()
sleep(2)
# driver.swich_to.alert.dismiss()
message=driver.switch_to.alert.text
print(message)




