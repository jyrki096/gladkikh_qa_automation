from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
try:
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element_by_id("button")

    #assert "successful" in message.text
finally:
    time.sleep(5)
    browser.quit()