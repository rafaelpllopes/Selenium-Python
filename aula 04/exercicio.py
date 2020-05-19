#! python3
from selenium.webdriver import Firefox
from time import sleep


"""
    Trabalhando com seletores css
    http://selenium.dunossauro.live/exercicio_05.html
    http://selenium.dunossauro.live/exercicio_06.html
    Zerar o https://flukeout.github.io
"""

url_exercicio05 = 'http://selenium.dunossauro.live/exercicio_05.html'
url_exercicio06 = 'http://selenium.dunossauro.live/exercicio_06.html'

firefox = Firefox()

firefox.get(url_exercicio05)
sleep(2)

firefox.quit()