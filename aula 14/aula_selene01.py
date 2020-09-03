from selene.support.shared import browser

browser.config.base_url = 'chrome'
browser.config.base_url = 'https://selenium.dunossauro.live'
browser.config.timeout = 10
browser.config.start_maximized = True

browser.open('/caixinha')
