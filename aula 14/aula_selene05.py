from selene import Browser, Config
from selenium.webdriver import Firefox

"""
    Element
"""

browser = Browser(
    Config(
        driver=Firefox(),
        base_url='https://selenium.dunossauro.live',
        timeout=30
    )
)

browser.open('/aula_07')
elementos = browser.all('input')

elementos[0].type('rafael')
elementos[1].type('rafael@rafael')
elementos[2].type('rafael')
elementos[3].press_enter()


