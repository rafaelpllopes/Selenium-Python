#! python3
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    EventFiringWebDriver,
    AbstractEventListener
)
from urllib.parse import urlparse
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

def page_1(driver):
    pass

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
        print(url)

    def before_click(self, element, driver):
        print(f'Elemento selecionado {element.tag_name}')

    def before_quit(self, driver):
        sleep(3)


browser = Firefox()
browser.implicitly_wait(30)
wrapper_browser = EventFiringWebDriver(browser, Escuta())

url = {
       1: 'http://selenium.dunossauro.live/exercicio_07.html',
       2: 'http://selenium.dunossauro.live/exercicio_03.html'
}

"""
    Exercicio 7: pegar as mudanças nas label atraves dos eventos
"""

wrapper_browser.get(f'{url[1]}')

nome = wrapper_browser.find_element_by_id('nome')
email = wrapper_browser.find_element_by_id('email')
senha = wrapper_browser.find_element_by_id('senha')
btn = wrapper_browser.find_element_by_id('btn')

nome.send_keys('teste')
email.send_keys('teste@teste')
senha.send_keys('senhaSenhaSENHA')
btn.click()

"""
    Exercicio 03: Refazer o exercicio, utilizar Escuta para gerar as ações
"""

def navegar(browser, seletor, sequencia=0, url_anterior=None):
    """
    Clicar em um link de acordo com seletor
        - browser: instancia do navegador
        - seletor: html [main, aside, ...]
        - sequencia: percorre o proximo item
        - url_anterior: lembrar ultima url para retornar pagina
    """

    url_atual = urlparse(browser.current_url)

    print(f'Escolhida a {sequencia+1}ª opção na url {url[2]}{url_atual.path}')
              
    if url_atual.path == '/diabao.html':

        if url_atual.path == '/page_4.html':
            browser.refresh()
        else:
            browser.get(f'{url[2]}{url_anterior}')
            sequencia += 1
            if sequencia > 1:
                sequencia = 0
            navegar(browser, 'main', sequencia, url_anterior)
    else:
        if url_atual.path == '/page_2.html':
            sleep(45)
            
    if url_atual.path != '/page_4.html':
        item = browser.find_element_by_tag_name(seletor)
        ancora = item.find_elements_by_tag_name('a')
        ancora[sequencia].click()
        navegar(browser, 'main', url_anterior=url_atual.path)
    else:
        browser.refresh()

wrapper_browser.get(url[2])     
comecar = wrapper_browser.find_element_by_css_selector('main li a')
comecar.click()

navegar(wrapper_browser, 'main')

wrapper_browser.quit()