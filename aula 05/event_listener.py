#! python3
from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.support.events import (
    EventFiringWebDriver,
    AbstractEventListener
)

"""
    O dispador de eventos é uma "burocracia" do selenium para usar um Listener
    Ele constrói um wrapper do webdriver e dispara os eventos para o Listener
"""


class Escuta(AbstractEventListener):
    """
        Classe para ouvir o clique antes
    """

    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'Antes do clck no {elemento.tag_name}')

    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'Depois do clck no {elemento.tag_name}')

    def after_navigate_to(self, elemento, webdriver):
        print(f'Indo para {url}')

    def after_navigate_back(self, webdriver):
        print('Voltando para página anterior')


browser = Firefox()
browser.implicitly_wait(30)
wrapper_browser = EventFiringWebDriver(browser, Escuta())

url = 'http://selenium.dunossauro.live/aula_07_d.html'
wrapper_browser.get(url)

texto = wrapper_browser.find_element_by_name('nome')
span = wrapper_browser.find_element_by_tag_name('span')
p = wrapper_browser.find_element_by_tag_name('p')

texto.click()
span.click()

wrapper_browser.get('http://selenium.dunossauro.live/aula_07_a.html')
wrapper_browser.back()

wrapper_browser.quit()
