from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    button.click()
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Franz")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Liszt")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Doboryan")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Austria")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
