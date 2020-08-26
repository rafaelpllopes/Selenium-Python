from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    text_to_be_present_in_element,
    text_to_be_present_in_element_value
)

url = 'https://selenium.dunossauro.live/aula_10_d.html'
browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 60)

locator_nome = (By.CSS_SELECTOR, 'input[name="nome"]')

wdw.until(
    text_to_be_present_in_element_value(
        locator_nome, 
        'disponível'
        )
)

browser.find_element(*locator_nome).send_keys('Teste')

wdw.until(
    text_to_be_present_in_element_value(
        ('css selector', 'input[name="email"]'), 
        'disponível'
        )
)

browser.find_element('css selector', 'input[name="email"]').send_keys('test@teste')
