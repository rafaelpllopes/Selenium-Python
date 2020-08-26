from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 60)

locator = (By.TAG_NAME, 'button')
button = browser.find_element(*locator)

wdw.until(
    element_to_be_clickable(locator), 'Elemento é clicavel, espera de  60 seg'
)

button.click()

texto = browser.find_element_by_tag_name('p').text

assert 'que' in texto

browser.quit()