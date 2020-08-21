#!python3
from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

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
def esperar_elemento(by, elemento, webdriver):
    """
        Verifica se o elemento está na tela.
    """
    print(f'Tentando encontrar "{elemento}" by {by}')
    if webdriver.find_elements(by, elemento):
        return True

    return False

esperar_botão = partial(esperar_elemento, By.CSS_SELECTOR, 'button')

wdw.until(esperar_botão)

# Clicar no botão
btn = browser.find_element_by_css_selector('button')
btn.click()

wdw.until(
    partial(esperar_elemento, By.ID, 'finished'),
    'A mensagem de sucesso não apareceu'
)

sucesso = browser.find_element_by_id('finished')
assert sucesso.text == 'Carregamento concluído'
print(sucesso.text)

browser.quit()



