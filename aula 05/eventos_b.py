#! python3
from selenium.webdriver import Firefox

browser = Firefox()
browser.implicitly_wait(30)
url = 'http://selenium.dunossauro.live/aula_07_b.html'

try:
    browser.get(url)
except:
    browser.quit()