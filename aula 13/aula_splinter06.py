from splinter import Browser

"""
   Interagir com elementos, utilizando fill para preencher
"""
with Browser() as browser: # Firefox browser default
    url = 'https://selenium.dunossauro.live/aula_07.html'
    browser.visit(url)
    browser.fill('nome', 'rafael')
    browser.fill('email', 'rafael@rafael')
    browser.fill('senha', '123')
   #  browser.find_by_value('Enviar!').click()
    browser.find_by_id('btn').click()
