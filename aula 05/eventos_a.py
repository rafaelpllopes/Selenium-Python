#! python3
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.implicitly_wait(30)

try:
    browser.get('http://selenium.dunossauro.live/aula_07_a.html')
    selected_item = browser.find_element_by_tag_name('svg')
    sleep(5)
except:
    browser.quit()
