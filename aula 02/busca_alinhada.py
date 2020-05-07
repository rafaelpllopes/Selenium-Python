#! python3
from selenium.webdriver import Firefox
from time import sleep

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

def find_by_href(browser, link):
    """
    Encontrar o elemento com o texto `text`.

    Argumento:
        - browser = Instancia do browser [firefox, chrome, ...]
        - link = link que será procurado em todas as tags `a
    """
    elements = browser.find_elements_by_tag_name('a')

    for element in elements:
        if link in element.get_attribute('href'):
            return element

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')
sleep(0.5)

elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')
print(elemento_ddg.text)

elemento_link_ddg = find_by_href(browser, 'ddg')
print(elemento_link_ddg.get_attribute('href'))

browser.quit()