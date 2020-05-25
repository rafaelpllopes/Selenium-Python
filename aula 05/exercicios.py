#! python3
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    EventFiringWebDriver,
    AbstractEventListener
)
from time import sleep

"""
       1. Pegar os estado do form
       2. Refazer o exercicio 3, usar o EventListener para printar o after de nageção e de clicks
       
       Extras:
              - Assistir a Live de Python #61 - Introdução a orientação a obejtos
              - Assistir a Live de Python #68 - Interfaces de ABCs
              - Assistir a Live de Python #115 - Introdução aos padrões de projetos
              - Assistir a Live de Python #117 - Padrão template method
"""

browser = Firefox()
browser.implicitly_wait(30)
url = {1: 'http://selenium.dunossauro.live/exercicio_07.html',
       2: 'http://selenium.dunossauro.live/exercicio_03.html'}

browser.get(url[1])
