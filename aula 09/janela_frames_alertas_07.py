from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located
)

from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/aula_11_c.html'
browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 60)

wdw.until(
    visibility_of_element_located((By.TAG_NAME, 'button'))
)

browser.find_element_by_tag_name('button').click()

print(browser.current_window_handle)
print(browser.window_handles)
# browser.quit()