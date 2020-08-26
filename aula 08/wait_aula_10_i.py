from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    title_contains,
    title_is
)

url = 'https://selenium.dunossauro.live/aula_10_c.html'
browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 30)

link = browser.find_elements_by_css_selector('.body_b a')

link[0].click()

wdw.until(
    title_contains('Aula')
)

wdw.until(
    title_is('Aula 10b')
)