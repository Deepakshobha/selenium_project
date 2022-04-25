from selenium.webdriver import Chrome
from time import sleep
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
#/session
driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.minimize_window()
current_url = driver.title
url = driver.current_url
# driver.close()
#sleep(1)
# driver.find_element_by_link_text("Register").click()
# sleep(1)
# driver.find_element_by_id("gender-female").click()
# sleep(1)
# driver.find_element_by_name("FirstName").send_keys("shobha")
# driver.find_element_by_name("LastName").send_keys("P")

# print(current_url)
# print(url)
