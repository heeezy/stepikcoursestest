from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
link='http://suninjuly.github.io/selects1.html'
browser=webdriver.Chrome()
try:
    browser.get(link)
    x=browser.find_element_by_css_selector('#num1').text
    y=browser.find_element_by_css_selector('#num2').text
    sum1=int(x)+int(y)
    select=Select(browser.find_element_by_css_selector('select[id=dropdown]'))
    select.select_by_value(str(sum1))
    browser.find_element_by_css_selector('button[type=submit]').click()
finally:
    time.sleep(5)
    browser.quit()

