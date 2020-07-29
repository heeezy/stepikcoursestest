from selenium import webdriver
import time,math
link='http://suninjuly.github.io/redirect_accept.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser=webdriver.Chrome()
browser.get(link)
time.sleep(2)
browser.find_element_by_css_selector('.trollface').click()
window1=browser.window_handles[0]
window2=browser.window_handles[1]
browser.switch_to.window(window2)
time.sleep(2)
x=calc(browser.find_element_by_css_selector("#input_value").text)
input1=browser.find_element_by_css_selector('#answer')
input1.send_keys(x)
btn1=browser.find_element_by_css_selector("button[type='submit']")
btn1.click()
time.sleep(5)
browser.quit()