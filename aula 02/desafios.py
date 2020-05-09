#! python3
"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Nevegar até o exercício 3
    achar a url do exercicio 3 e ur até la
"""
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
from urllib.parse import urlparse

browser = Firefox()

url_padrao = 'http://selenium.dunossauro.live'

browser.get(f'{url_padrao}/aula_04.html')
sleep(10)

def get_links(browser, elemento): # dicionario
    """
    pega todos os links dentro de um elemento

    - browser = a instancia do navegador
    - elemento = webelement [aside, ,main, body, ...]
    """

    selecionado = browser.find_element_by_tag_name(elemento)
    elemento_ancoras = selecionado.find_elements_by_tag_name('a')

    resultado = {}

    for ancora in elemento_ancoras:
        resultado.update({ancora.text: ancora.get_attribute('href')})

    return resultado

"""
Parte 1
"""
aulas = get_links(browser, 'aside')
pprint(aulas)

"""
browser.get(aside['Aula 3'])
browser.get(aside['Aula 4'])
"""

"""
Parte 2
"""

exercicios = get_links(browser, 'main')
pprint(exercicios)
browser.get(exercicios['Exercício 3'])

"""
Parte 3
    - Exercicio 3
"""

def navegar(browser, seletor, sequencia=0, url_anterior=None):
    """
    Clicar em um link de acordo com seletor
        - browser: instancia do navegador
        - seletor: html [main, aside, ...]
        - sequencia: percorre o proximo item
        - url_anterior: lembrar ultima url para retornar pagina
    """
    sleep(5)

    url = urlparse(browser.current_url)

    print(f'Escolhida a {sequencia+1}ª opção na url {url_padrao}{url.path}')
              
    if url.path == '/diabao.html':

        if url.path == '/page_4.html':
            browser.refresh()
        else:
            browser.get(f'{url_padrao}{url_anterior}')
            sequencia += 1
            if sequencia > 1:
                sequencia = 0
            navegar(browser, 'main', sequencia, url_anterior)
    else:
        if url.path == '/page_2.html':
            sleep(30)
            
    if url.path != '/page_4.html':
        item = browser.find_element_by_tag_name(seletor)
        ancora = item.find_elements_by_tag_name('a')
        ancora[sequencia].click()
        navegar(browser, 'main', url_anterior=url.path)
    else:
        browser.refresh()
    
    sleep(3)
    browser.quit()
           

navegar(browser, 'main')