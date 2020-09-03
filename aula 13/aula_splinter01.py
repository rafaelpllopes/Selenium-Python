from splinter import Browser

with Browser(headless=True) as browser: # Firefox browser default
    url = 'https://google.com'
    browser.visit(url)
    print(browser.is_element_present_by_name('q'))

"""
    headless: Carrega sem que o browser esteja visivel
"""
with Browser(headless=True) as browser:
    url = 'https://google.com'
    browser.visit(url)
    print(browser.is_element_present_by_name('q'))


"""
    incognito: o browser abre em modo privado
"""
with Browser(incognito=True) as browser:
    url = 'https://google.com'
    browser.visit(url)
    print(browser.is_element_present_by_name('q'))
        
"""
    mudar o browser
"""
with Browser('chrome') as browser:
    url = 'https://google.com'
    browser.visit(url)
    print(browser.is_element_present_by_name('q'))

"""
    mudar o browser, abrir no modo anonimo
"""
with Browser('chrome', incognito=True) as browser:
    url = 'https://google.com'
    browser.visit(url)
    print(browser.is_element_present_by_name('q'))