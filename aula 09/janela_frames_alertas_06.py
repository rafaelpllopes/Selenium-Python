from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located,
    new_window_is_opened
)

from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/aula_11_b.html'
browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 60)

print(browser.current_window_handle)
print(browser.window_handles)

wdw.until(
    visibility_of_element_located((By.ID, 'popup'))
)

browser.find_element_by_id('popup').click()

def find_window(content: str):
    wids = browser.window_handles

    for window in wids:
        browser.switch_to.window(window)
        if content in browser.page_source.lower():
            break

wdw.until(
    new_window_is_opened
)

find_window('popup')
# browser.quit()