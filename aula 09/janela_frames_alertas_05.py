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
    visibility_of_element_located((By.ID, 'all'))
)

browser.find_element_by_id('all').click()

alert = Alert(browser)

wdw.until(
    alert_is_present()
)

alert.accept() # alert
alert.send_keys('Rafael') # prompt
alert.accept() # prompt
alert.accept() # confirm

browser.find_element_by_id('alertd').click()
alertd = wdw.until(alert_is_present()) # Esperar o alert, retorna o alerta
alertd.accept()

browser.quit()