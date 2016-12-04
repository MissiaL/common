#!/usr/bin/env python
# coding: utf-8

"""
Кандидату, претендующему на вакансию «Инженер по автоматизации тестирования» нужно решить следующую задачу: написать сценарий для Selenium c использованием RSpec и Watir WebDriver.

СЦЕНАРИЙ ДОЛЖЕН ОСУЩЕСТВЛЯТЬ ОПИСАННЫЕ НИЖЕ ДЕЙСТВИЯ:
1. Открыть браузер и развернуть на весь экран.
2. Зайти на yandex.ru.
3. В разделе маркет выбрать Сотовые телефоны.
4. Зайти в расширенный поиск.
5. Задать параметр поиска до 20000 рублей
6. Нажать кнопку Подобрать.
ПРИМЕЧАНИЯ:
Предполагается полная свобода в действиях. При оценке в обязательном порядке будут учитываться:
- работоспособность сценария в браузерах Google Chrome и Mozilla Firefox
- «живучесть» сценария (обработка ошибок и исключений);
"""

# Решение

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROMEDRIVER = r"C:\Selenium\chromedriver\chromedriver.exe"


def wait_elem_visible(xpath):
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, xpath)))
    return element


driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
try:
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://market.yandex.ru/")
    driver.find_element_by_xpath("/html/body/div/div[2]/noindex/ul/li[1]/a").click()
    wait_elem_visible("/html/body/div[1]/div[4]/div[1]/div/div[1]/div/a[1]").click()
    wait_elem_visible("/html/body/div[1]/div[4]/div[2]/div[2]/div[1]/div/div[38]/div[2]/a").click()
    # Зададим цену
    wait_elem_visible('//*[@id="glf-priceto-var"]').send_keys(u"20000")
    # Нажмем на поиск
    wait_elem_visible("/html/body/div[1]/div[4]/div/div[1]/div[4]/a[2]").click()
    # Дождемся результатов поиска
    wait_elem_visible("/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]")
finally:
    driver.quit()
