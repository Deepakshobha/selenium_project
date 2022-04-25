from selenium.webdriver import Chrome
# from selenium.webdriver.support.select import Select
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get("https://www.myntra.com/kids?f=Categories%3ATshirts%3A%3AGender%3Aboys%2Cboys%20girls&plaEnabled=false")
# driver.find_element_by_xpath("//a[text()='Women']")
# driver.find_element_by_xpath("//a[text()='Ethnic Wear']/../..//li[@class='desktop-oddColumnContent']").click()
# driver.find_element_by_xpath("//input[@value='Pantaloons Junior']/../..//label[@class='vertical-filters-label common-customCheckbox']").click()
# driver.find_element_by_xpath("//label[@class='common-customCheckbox vertical-filters-label']").click()
driver.find_element_by_xpath("//input[@value='2569.0 TO 3784.0']/../..//label[@class='common-customCheckbox vertical-filters-label']").click()
