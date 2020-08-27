from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    new_window_is_opened,
    number_of_windows_to_be
)

url = 'https://selenium.dunossauro.live/aula_11_c.html'
browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 10)

browser.execute_script('window.open()')

wdw.until(
    new_window_is_opened(browser.window_handles)
)

wdw.until(
    number_of_windows_to_be(2)
)

browser.switch_to.window(browser.window_handles[-1])
browser.get('http://ddg.gg')

