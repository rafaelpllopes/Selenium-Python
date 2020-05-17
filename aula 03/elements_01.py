#! python3

from selenium.webdriver import Firefox
from time import sleep

firefox = Firefox()

url_base = 'http://selenium.dunossauro.live'

"""
    Buscando elementos por Id
"""
firefox.get(f'{url_base}/aula_05_a.html')
sleep(1)
div_py = firefox.find_element_by_id('python')
div_hk = firefox.find_element_by_id('haskell')
print(div_py.text)
print(div_hk.text)

firefox.quit()