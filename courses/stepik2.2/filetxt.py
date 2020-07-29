from selenium import webdriver
import time, os
link='http://suninjuly.github.io/file_input.html'
browser=webdriver.Chrome()
browser.get(link)
browser.find_element_by_css_selector('input[name=firstname]').send_keys('Vanya')
browser.find_element_by_css_selector('input[name=lastname]').send_keys('trr')
browser.find_element_by_css_selector('input[name=email]').send_keys('gg@gg')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.dirname(__file__))
browser.find_element_by_css_selector('input[id=file]').send_keys(file_path)
browser.find_element_by_css_selector('button[type=submit]').click()
time.sleep(10)
browser.quit()