from selenium import webdriver
import math
import time
browser=webdriver.Chrome()
link='http://suninjuly.github.io/get_attribute.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser.get(link)
    treasure=browser.find_element_by_css_selector("img['#treasure']").get_attribute('valuex')
    x=calc(treasure)
    input1=browser.find_element_by_css_selector('#answer')
    input1.send_keys(x)
    checkbox1=browser.find_element_by_css_selector('#robotCheckbox')
    checkbox1.click()
    radiobutton1=browser.find_element_by_css_selector("#robotsRule")
    radiobutton1.click()
    btn1=browser.find_element_by_css_selector("button[type='submit']")
    btn1.click()
finally:
    time.sleep(5)
    browser.quit()
