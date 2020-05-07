#! python3

from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

def find_by_text(browser, tag, text):
    """
    Encontrar o elemento com o texto `text`.

    Argumento:
        - browser = Instancia do browser [firefox, chrome, ...]
        - texto = conteúdo que deve estar na tag
        - tag = tag onde o texto será procurado
    """
    elements = browser.find_elements_by_tag_name(tag)

    for element in elements:
        if element.text == text:
            return element

browser.get('http://selenium.dunossauro.live/aula_04_b.html')
sleep(0.5)

nome_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nome_das_caixas:
    find_by_text(browser, 'div', nome).click()
    sleep(0.3)

for nome in nome_das_caixas:
    browser.back()
    sleep(0.3)

for nome in nome_das_caixas:
    browser.forward()
    sleep(0.3)

browser.quit()