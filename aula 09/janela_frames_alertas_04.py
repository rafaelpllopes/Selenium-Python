from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
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
    visibility_of_element_located((By.ID, 'confirm'))
)

browser.find_element_by_id('confirm').click()

alert = Alert(browser)

wdw.until(
    alert_is_present()
)

print(alert.text)
alert.accept()