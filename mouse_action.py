# from selenium.webdriver import Chrome
# # from selenium.webdriver.support.select import Select
# driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
# driver.get("file:///C:/Users/Deepak%20M/Desktop/selenium/demo-html/demo.html")
# eles=driver.find_elements_by_xpath("//table[@name='customers']//td[2]")
# names = [fname.text for fname in eles]
# print(names)
#
# sorted_text = sorted(names)
#
# if names == sorted_text:
#     print(True)
# else:
#     print(False)



from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get("https://www.myntra.com/kids?f=Categories%3ATshirts%3A%3AGender%3Aboys%2Cboys%20girls&plaEnabled=false")
actions=ActionChains(driver)


# profile=driver.find_element_by_xpath("//span[@class='myntraweb-sprite desktop-iconUser sprites-headerUser']")
# actions.move_to_element(profile).perform()
# driver.find_element_by_xpath("//a[@class='desktop-linkButton']").click()


content=driver.find_element_by_xpath("//a[text()='Women']")
actions.move_to_element(content).perform()
driver.find_element_by_xpath("//a[text()='Sarees']").click()



