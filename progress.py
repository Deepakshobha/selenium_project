# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
# driver.get("file:///C:/Users/Deepak%20M/Desktop/selenium/demo-html/progressbar.html")
# driver.find_element_by_xpath("//button[text()='Click Me']").click()
# wait=WebDriverWait(driver,20)
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         print("calling __call__")
#         result = super().__call__(driver)
#         #cheking __call__ has returned a webelement
#         if isinstance(result,WebElement):
#             return result.is_enabled()  #is_enabled method on webelement
#         return False
# v =_visibility_of_element_located(("name","fname"))
# wait.until(v) #calls the call method present visibility class


from selenium.webdriver import Chrome
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get("http://demowebshop.tricentis.com/")

def enter_text(loctype,locvalue,value):
    driver.find_element(loctype, locvalue).send_keys(value)

def click_element(loctype,locvalue,value):
    driver.find_element("loctype", "locvalue").click()

driver.find_element("link text","Register").click()
driver.find_element("id","gender-female")
driver.find_element("name","FirstName").send_keys("shobha")
driver.find_element("name","LastName").send_keys("P")
driver.find_element_by_name("Email").send_keys("shobhahdp@gmail.com")
driver.find_element_by_id("Password").send_keys("shobha123")
driver.find_element_by_id("ConfirmPassword").send_keys("shobha123")
driver.find_element_by_name("register-button")




