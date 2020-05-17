#! python3

from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep

"""
    Desafio:
        - Preencher o formulario
        - Enviar dados do formulario
        - Pegar a url de resultado e fazer o assert da query
"""
firefox = Firefox()

url = 'http://selenium.dunossauro.live/exercicio_04.html'
firefox.get(url)

sleep(3)
firefox.quit()