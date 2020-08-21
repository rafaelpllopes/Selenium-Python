#!python3
from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://selenium.dunossauro.live/aula_09_a.html'

browser = Firefox()

wdw = WebDriverWait(
    browser, 
    30,
    poll_frequency=0.5,
    ignored_exceptions=None
)

# Abrir a pagina
browser.get(url)

# Esperar o botão
def esperar_elemento(elemento, webdriver):
    """
        Verifica se o elemento está na tela.
    """
    print(f'Tentando encontrar "{elemento}"')
    if webdriver.find_elements_by_css_selector(elemento):
        return True

    return False

esperar_botão = partial(esperar_elemento, 'button')
esperar_sucesso = partial(esperar_elemento, '#finished')

wdw.until(esperar_botão)

# Clicar no botão
btn = browser.find_element_by_css_selector('button')
btn.click()

wdw.until(esperar_sucesso, 'A mensagem de sucesso não apareceu')
sucesso = browser.find_element_by_id('finished')
assert sucesso.text == 'Carregamento concluído'
print(sucesso.text)

browser.quit()



