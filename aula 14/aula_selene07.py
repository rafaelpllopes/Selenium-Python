from selene import Browser, Config
from selenium.webdriver import Firefox
from selene.support import by
from selene.support.conditions import not_, be, have

"""
    Validação
"""

browser = Browser(
    Config(
        driver=Firefox(),
        base_url='https://google.com',
    )
)

browser.open('')

browser.s(by.name('q')).should(be.blank).type('Live de python')

browser.s(by.name('q')).should(not_.blank).type('teste em python')

browser.s(by.name('q')).should(have.attribute('name').value('q'))

