from selenium import webdriver
browser=webdriver.Chrome()
browser.execute_script("document.title='ABRACADABRA';alert('Robots at work')")
browser.quit()