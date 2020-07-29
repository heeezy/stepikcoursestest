from selenium import webdriver
import time, math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link='http://suninjuly.github.io/alert_accept.html'
link2='https://stepik.org/lesson/184253/step/4?unit=158843'
browser=webdriver.Chrome()
browser.get(link)
browser.find_element_by_css_selector('button[type=submit]').click()
confirm=browser.switch_to.alert
confirm.accept()
x=browser.find_element_by_css_selector('#input_value').text
otv=calc(int(x))
browser.find_element_by_css_selector('#answer').send_keys(otv)
browser.find_element_by_css_selector('button[type=submit]').click()
alert=browser.switch_to.alert
alert_text=alert.text
otv2=str(alert_text.split(': ')[-1])
alert.accept()
print(otv2)
time.sleep(4)
browser.get(link2)
time.sleep(10)
browser.find_element_by_css_selector('#ember4706').send_keys(otv2)
browser.find_element_by_css_selector('.submit-submission').click()
