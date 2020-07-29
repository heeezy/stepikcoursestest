from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.first_class > input")
    input1.send_keys("name")
    input2 = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.second_class > input")
    input2.send_keys("last")
    input3 = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.third_class > input")
    input3.send_keys("mail")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()