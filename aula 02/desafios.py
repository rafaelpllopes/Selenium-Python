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

browser.get('http://selenium.dunossauro.live/aula_04.html')
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

def navegar(browser, seletor, sequencia=0):
    """
    Clicar em um link de acordo com seletor
        - browser: instancia do navegador
        - seletor html [main, aside, ...]
    """
    sleep(10)
    item = browser.find_element_by_tag_name(seletor)
    ancora = item.find_elements_by_tag_name('a')
    ancora[sequencia].click()
    sleep(10)
    url = urlparse(browser.current_url)
    
    print(sequencia, url.path)
    
    if url.path == '/diabao.html':
        sleep(10)
        item = browser.find_element_by_tag_name('main')
        texto = item.find_element_by_tag_name('p').text
        if 'refresh' in texto:
            browser.refresh()
            sleep(10)
        
        if 'erro' in texto:
            browser.back()
            sequencia += 1
            navegar(browser, 'main', sequencia)
    
    if url.path != '/page_4.html':
        navegar(browser, 'main')

    browser.quit()
           

navegar(browser, 'main')