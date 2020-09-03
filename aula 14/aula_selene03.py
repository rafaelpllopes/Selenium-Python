from selene import Browser, Config
from selenium.webdriver import Firefox

"""
    Navegação

    Selenium | Selene
    get() | open()
    back() | driver.back()
    forward() | driver.forward()
    current_url | driver.current_url
    title | driver.title
    page_source | driver.page_source
"""

browser = Browser(
    Config(
        driver=Firefox(),
        base_url='https://selenium.dunossauro.live',
        timeout=10
    )
)

browser.open('/keyboard')
print(browser.driver.current_url)
browser.open('/caixinha')
print(browser.driver.current_url)


