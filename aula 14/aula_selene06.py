from selene import Browser, Config
from selenium.webdriver import Firefox
from selene import by

"""
    Element
"""

browser = Browser(
    Config(
        driver=Firefox(),
        base_url='https://google.com',
        timeout=30
    )
)

browser.open('')
browser.element(by.name('q')).type('Live de python').press_enter()


