from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')

wait15=WebDriverWait(browser,15)
wait15.until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
button = browser.find_element_by_css_selector("#book")
button.click()
x=calc(browser.find_element_by_css_selector("#input_value").text)
input1=browser.find_element_by_css_selector('#answer')
input1.send_keys(x)
btn1=browser.find_element_by_css_selector("button[type='submit']")
btn1.click()
time.sleep(5)
browser.quit()