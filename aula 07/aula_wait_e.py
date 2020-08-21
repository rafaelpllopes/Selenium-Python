#!python3
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
class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):
            return True
        return False

locator = (By.CSS_SELECTOR, 'button')
esperar_botão = EsperarElemento(locator)

wdw.until(esperar_botão)

# Clicar no botão
btn = browser.find_element_by_css_selector('button')
btn.click()

wdw.until(
    EsperarElemento((By.ID, 'finished')),
    'A mensagem de sucesso não apareceu'
)

sucesso = browser.find_element_by_id('finished')
assert sucesso.text == 'Carregamento concluído'
print(sucesso.text)

browser.quit()



