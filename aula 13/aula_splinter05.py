from splinter import Browser

"""
   Interagir com elementos
"""
with Browser() as browser: # Firefox browser default
    url = 'https://selenium.dunossauro.live/aula_07.html'
    browser.visit(url)
    browser.find_by_id('nome').type('rafael')
    browser.find_by_id('email').type('rafael@rafael')
    browser.find_by_id('senha').type('123')
    browser.find_by_id('btn').click()
