from selene import Browser, Config
from selenium.webdriver import Firefox

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
# browser.element('input[name="q"]').type('live de python')
browser.element('//*[@name="q"]').type('live de python').press_enter()


