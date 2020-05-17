#! python3

from selenium.webdriver import Firefox
from time import sleep

firefox = Firefox()

url_base = 'http://selenium.dunossauro.live'

"""
    Preencher formularios
"""

firefox.get(f'{url_base}/aula_05_c.html')
sleep(1)

# filme = firefox.find_element_by_name('filme')
# filme.send_keys('Parisita')

# email = firefox.find_element_by_name('email')
# email.send_keys('teste@teste')

# telefone = firefox.find_element_by_name('telefone')
# telefone.send_keys('(015)999999999')

# input_enviar = firefox.find_element_by_name('enviar')
# input_enviar.click()

def melhor_filme(browser, filme, email, telefone):
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()

melhor_filme(firefox, 'Parasita', 'teste@teste', '(015)999999999')

sleep(3)
firefox.quit()