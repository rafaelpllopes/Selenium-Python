#!python3
from selenium.webdriver import Firefox

url = 'https://selenium.dunossauro.live/aula_09_a.html'

browser = Firefox()

browser.get(url)

browser.implicitly_wait(30)

btn = browser.find_element_by_css_selector('button')
btn.click()

sucesso = browser.find_element_by_id('finished')
assert sucesso.text == 'Carregamento concluído'

