from splinter import Browser

"""
   Marchers
"""
browser = Browser() 
url = 'https://selenium.dunossauro.live/aula_09_a.html'
browser.visit(url)

if browser.is_text_present('Barrinha top', wait_time=60):
       browser.find_by_text('Barrinha top').click()
