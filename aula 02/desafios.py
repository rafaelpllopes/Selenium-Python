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

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04.html')
sleep(0.5)

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