# from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
# from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
# driver.get("file:///C:/Users/Deepak%20M/Desktop/selenium/demo-html/loading.html")
# wait=WebDriverWait(driver,20) #maximum time 20s
# v = visibility_of_element_located(("name","fname"))
# wait.until(v) #calls the call method present visibility class
# driver.find_element_by_name("fname").send_keys("hello")

#__call_ method returns either webelement if the element is visible on the webpage otherwise it returnsFalse
# untill method keeps calling __call__method of visibility_of_element_located class in the time interval of 0.5sec. If untill method
#recevies webelement from __call__method, then it is understood that the element is visible on th page
# If untill method recevices bool False, then it is understood that the elememt is not yet visible on the webpage
#untill method will raise Timeout exception if the it keeps receving bool False from __call__method even after maximum timeout period

#explicit wait
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get(r"http://demowebshop.tricentis.com")
class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        print("calling __call__")
        result = super().__call__(driver)
        #cheking __call__ has returned a webelement
        if isinstance(result,WebElement):
            return result.is_enabled()  #is_enabled method on webelement
        return False



def wait(func):
    def wrapper(*args,**kwargs):
        locator = args[0]
        wait = WebDriverWait(driver, 20)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args,**kwargs)
    return wrapper

@wait
def enter_text(locator, *, Value):
    driver.find_element(*locator).send_keys(Value)
@wait
def click_ele(locator):
    driver.find_element(*locator).click()
# @wait
# def select_item(locator,*,item):
#     element = driver.find_element(*locator)
#     s = Select(element)
#     s.select_by_visible_text(item)


click_ele(("link text","Register"))
click_ele(("id","gender-male"))
enter_text(("id","FirstName"),Value="hello")
# sect_items(('id','standard_cars'),item="mercedees")






# implicit Synchroniztion
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
#
# driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
# driver.implicitly_wait(2)  # wait for time  by default implicitly_wait time is 0
# driver.get("http://demowebshop.tricentis.com/")
# driver.find_element_by_link_text("Register")
