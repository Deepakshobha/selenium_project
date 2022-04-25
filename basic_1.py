from selenium.webdriver import Chrome
from time import sleep
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get("http://demowebshop.tricentis.com/")
# lnk_register=driver.find_element_by_class_name("ico-register").click(
driver.find_element_by_css_selector("a[class='ico-register']").click()
# # lnk_register=driver.find_element_by_link_text("Register").click()
# # # sleep(1)
# id_=driver.find_element_by_id("gender-female")
# id_.click()
#
# # id_=driver.find_element_by_name("gender-female").click()
# # sleep(1)
# name_f=driver.find_element_by_name("FirstName").send_keys("shobha")
# name_l= driver.find_element_by_name("LastName")
# name_l.send_keys("P")
#
# email= driver.find_element_by_name("Email").send_keys("shobhahdp@gmail.com")
# password=driver.find_element_by_id("Password").send_keys("shobha123")
# c_password=driver.find_element_by_id("ConfirmPassword").send_keys("shobha123")
# btn= driver.find_element_by_name("register-button")
# btn.click()



