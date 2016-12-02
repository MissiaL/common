#!/usr/bin/env python
# coding: utf-8

"""
Кандидату, претендующему на вакансию «Инженер по автоматизации тестирования» нужно решить следующую задачу: написать сценарий для Selenium c использованием RSpec и Watir WebDriver.

СЦЕНАРИЙ ДОЛЖЕН ОСУЩЕСТВЛЯТЬ ОПИСАННЫЕ НИЖЕ ДЕЙСТВИЯ:
1. Открыть браузер и развернуть на весь экран.
2. Зайти на yandex.ru.
3. В разделе маркет выбрать Сотовые телефоны.
4. Зайти в расширенный поиск.
5. Задать параметр поиска до 20000 рублей и Диагональ экрана от 3 дюймов.
6. Выбрать не менее 5 любых производителей, среди популярных.
7. Нажать кнопку Подобрать.
8. Проверить, что элементов на странице 10.
9. Запомнить первый элемент в списке.
10. Изменить Сортировку на другую (популярность или новизна).
11. Найти и нажать по имени запомненного объекта.
12. Вывести цифровое значение его оценки.
13. Закрыть браузер.
ПРИМЕЧАНИЯ:
Предполагается полная свобода в действиях. При оценке в обязательном порядке будут учитываться:
- работоспособность сценария в браузерах Google Chrome и Mozilla Firefox
- гибкость и адаптивность сценария (насколько просто заменить часть исходных данных, например - города);
- «живучесть» сценария (обработка ошибок и исключений);
"""

# Решение

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

geckodriver = "/opt/geckodriver/geckodriver"

driver = webdriver.Firefox(executable_path=geckodriver)
driver.implicitly_wait(10)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://market.yandex.ru/")
driver.find_element_by_xpath("/html/body/div/div[2]/noindex/ul/li[1]/a").click()
driver.find_element_by_xpath("//a[contains(.,'Мобильные телефоны')]").click()
