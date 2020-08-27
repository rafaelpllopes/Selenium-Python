from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located,
    alert_is_present
)

from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/aula_11_a.html'
browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 30)

wdw.until(
    visibility_of_element_located((By.ID, 'alert'))
)

browser.find_element_by_id('alert').click()

alert = browser.switch_to.alert # Não lida com erros, tem que usar no momento que for necessario

wdw.until(
    alert_is_present()
)

print(alert.text)
alert.accept()