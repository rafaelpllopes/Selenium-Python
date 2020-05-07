#! python3

from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_b.html')
sleep(0.5)

url_parseada = urlparse(browser.current_url)
print(url_parseada)
browser.quit()