from selene import Browser, Config
from selenium.webdriver import Firefox

browser = Browser(
    Config(
        driver=Firefox(),
        base_url='https://selenium.dunossauro.live'
    )
)

browser.open('/caixinha')