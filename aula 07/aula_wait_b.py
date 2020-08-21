#!python3
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://selenium.dunossauro.live/aula_09_a.html'

browser = Firefox()

wdw = WebDriverWait(
    browser, 
    10,
    poll_frequency=0.1,
    ignored_exceptions=None
)

# Abrir a pagina
browser.get(url)

# Esperar o botão
def esperar_botao(webdriver):
    """
        Verifica se o elemento 'button' está na tela.
    """
    elements = webdriver.find_elements_by_css_selector('button')
    return bool(elements)

wdw.until(esperar_botao)

# Clicar no botão
btn = browser.find_element_by_css_selector('button')
btn.click()

def esperar_sucesso(webdriver):
    """
        Verifica se o elemento id finished
    """
    elemento = webdriver.find_element_by_id('finished')
    return bool(elemento)

wdw.until(esperar_sucesso, 'A mensagem de sucesso não apareceu')
sucesso = browser.find_element_by_id('finished')
assert sucesso.text == 'Carregamento concluído'
print(sucesso.text)



