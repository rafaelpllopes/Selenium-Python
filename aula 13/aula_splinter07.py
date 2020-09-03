from splinter import Browser

"""
   Interagir mouse
"""
browser = Browser() 
url = 'https://selenium.dunossauro.live/caixinha.html'
browser.visit(url)
caixa = browser.find_by_id('caixa')
caixa.click()

# AC
caixa.mouse_over()
caixa.double_click()
caixa.right_click()