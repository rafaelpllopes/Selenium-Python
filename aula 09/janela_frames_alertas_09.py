from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    frame_to_be_available_and_switch_to_it,
    element_to_be_clickable
)

url = 'https://selenium.dunossauro.live/aula_11_d.html'
browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 30)

wdw.until(
    frame_to_be_available_and_switch_to_it(
        ('name', 'iframe')
    )
)

browser.switch_to.frame('iframe')

wdw.until(
    element_to_be_clickable(
        ('id', 'nome')
    )
)

browser.find_element_by_id('nome').send_keys('teste')