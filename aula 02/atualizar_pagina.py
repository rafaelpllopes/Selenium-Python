#! python3

from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_b.html')
sleep(0.5)

browser.refresh()
sleep(0.5)
browser.refresh()
sleep(0.5)

browser.quit()