#! python3
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    EventFiringWebDriver,
    AbstractEventListener
)
from time import sleep

"""
       1. Pegar os estado do form
       2. Refazer o exercicio 3, usar o EventListener para printar o after de navegação e de clicks
       
       Extras:
              - Assistir a Live de Python #61 - Introdução a orientação a obejtos
              - Assistir a Live de Python #68 - Interfaces de ABCs
              - Assistir a Live de Python #115 - Introdução aos padrões de projetos
              - Assistir a Live de Python #117 - Padrão template method
"""

def print_components(components):
    for component in components:
        print(component.text)

class Escuta(AbstractEventListener):
    """
        Classe que ouve as ações na pagina
    """

    def before_change_value_of(self, element, driver):
        if element.tag_name == 'input':
            components = driver.find_elements_by_tag_name('label')
            print_components(components)

    def after_change_value_of(self, element, driver):
        if element.tag_name == 'input':
            components = driver.find_elements_by_tag_name('label')
            print_components(components)

    def after_navigate_to(self, url, driver):
        print(f'URL: {url}')      

browser = Firefox()
browser.implicitly_wait(30)
wrapper_browser = EventFiringWebDriver(browser, Escuta())

url = {
       1: 'http://selenium.dunossauro.live/exercicio_07.html',
       2: 'http://selenium.dunossauro.live/exercicio_03.html'
}

wrapper_browser.get(f'{url[1]}')

nome = wrapper_browser.find_element_by_id('nome')
email = wrapper_browser.find_element_by_id('email')
senha = wrapper_browser.find_element_by_id('senha')
btn = wrapper_browser.find_element_by_id('btn')

nome.send_keys('teste')
email.send_keys('teste@teste')
senha.send_keys('senhaSenhaSENHA')
btn.click()

wrapper_browser.quit()