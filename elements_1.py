# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
# driver.get("file:///C:/Users/Deepak%20M/Desktop/selenium/demo-html/demo.html")
# elements=driver.find_elements_by_name("download")
# print(type(elements))
# print(len(elements))
# print(elements)

# for item in elements:
#     print(item.click())

# for item in elements[::-1]:
#     print(item.click())




# boxes = driver.find_elements_by_name('fname')
# for item in boxes:
#     item.send_keys('hello')
#     sleep(1)


# li = ['apple','google','gmail','facebook','insta','whatsapp','asad','fdg','dhsjdh']
# boxes = driver.find_elements_by_name('fname')
# for box,item in zip(boxes,li):
#     box.send_keys(item)
#     sleep(1)


links = driver.find_elements_by_xpath("//a")
print(links)

for link in links:
    print(link.text)
    sleep(1)

