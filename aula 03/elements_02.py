#! python3

from selenium.webdriver import Firefox
from time import sleep

firefox = Firefox()

url_base = 'http://selenium.dunossauro.live'

"""
    Buscando elementos por classname
"""
firefox.get(f'{url_base}/aula_05_b.html')
sleep(1)
topico = firefox.find_element_by_class_name('topico')
linguagens = firefox.find_elements_by_class_name('linguagens')

print(topico.text)

for linguagem in linguagens:
    titulo = linguagem.find_element_by_tag_name('h2')
    paragrafo = linguagem.find_element_by_tag_name('p')
    print(f'{titulo.text}: {paragrafo.text}')

firefox.quit()