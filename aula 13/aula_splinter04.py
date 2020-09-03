from splinter import Browser

"""
   Interagir com elementos
"""
with Browser() as browser: # Firefox browser default
    url = 'https://google.com'
    browser.visit(url)
    browser.find_by_name('q').type('Live de python')
    browser.find_by_name('btnK').click()