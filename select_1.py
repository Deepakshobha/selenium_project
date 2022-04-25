from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
driver = Chrome(r"C:\Users\Deepak M\Desktop\training\chromedriver")
driver.get("file:///C:/Users/Deepak%20M/Desktop/selenium/demo-html/demo.html")
element = driver.find_element_by_id("standard_cars")
s = Select(element)
print(s)
# s.select_by_visible_text("Mercedes")
# sleep(1)
# s.select_by_visible_text("Audi")
# sleep(1)
# s.select_by_visible_text("Toyota")
# sleep(1)
# s.select_by_index(7)
# sleep(1)
# s.select_by_index(3)
# sleep(1)
# s.select_by_index(20) #exeception


# s.select_by_value("bmw") #attribute value always we go with visible text
# sleep(1)
# s.select_by_value("nin")
# sleep(1)


items=s.options                     #provides list option availe in list box
# text of all the items
for item in items:
    print(item.text)

# all_option = [item.text for item in items]


# for i in all_option:
#     s.select_by_visible_text(i)
#     sleep(1)

#select the item is availabe select and print the index of it
# for index,item in enumerate(all_option):
#     if item == "BMW":
#         s.select_by_visible_text(item)
#         print(f"the index of {item} is {index}")
#
# print(s.first_selected_option)
# print(s.first_selected_option.text)


#multiple selection
element = driver.find_element_by_id("multiple_cars")
s = Select(element)

# s.select_by_visible_text("Audi")
# sleep(1)
# s.select_by_visible_text("BMW")
# sleep(1)
# s.select_by_visible_text("Toyota")
# sleep(1)

# cars = ["Audi","BMW","Toyota"]
# for car in cars:
#     s.select_by_visible_text(car)
#     sleep(1)
#
# s.deselect_by_visible_text("BMW")
def select_all(list_box):
    s = Select(list_box)
    items = s.options
    data = [item.text for item in items]
    for item in data:
        s.select_by_visible_text(item)
        sleep(1)

select_all(element)
print(s.all_selected_options)

a = s.all_selected_options
for item in a:
    print(item.text)


