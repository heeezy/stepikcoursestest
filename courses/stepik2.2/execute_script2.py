from selenium import webdriver
import math, time
browser = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
x=browser.find_element_by_css_selector('#input_value').text
button1=browser.find_element_by_css_selector('button[type=submit]')
browser.execute_script("window.scrollBy(0, 150);")
browser.find_element_by_css_selector("input[id=answer]").send_keys(calc(x))
checkbox1 = browser.find_element_by_css_selector('#robotCheckbox')
checkbox1.click()
radiobutton1 = browser.find_element_by_css_selector("#robotsRule")
radiobutton1.click()
button1.click()
time.sleep(5)