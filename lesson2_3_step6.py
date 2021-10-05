from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    tx = browser.find_element_by_css_selector('[id="input_value"]')
    x = tx.text
    y = calc(x)
    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)
    button1 = browser.find_element_by_tag_name("button")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
