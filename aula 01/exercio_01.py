#! python3.8.2
from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

navegador = Firefox()
try:
    navegador.get(url)
    sleep(0.5)
    h1 = navegador.find_element_by_tag_name('h1')
    p = navegador.find_elements_by_tag_name('p')

    # Primeira forma para formar o dicionario

    dict_atributos = {}

    for item in p:
        dict_atributos.update(
            {item.get_attribute('atributo') : item.text}
        )

    dicionario = { h1.text : dict_atributos}
    print(dicionario)

    # Segunda forma de formar o dicionarios com Dictionary Comprehension

    dict_comprehension = {h1.text : {item.get_attribute('atributo') : item.text for item in p}}
    print(dict_comprehension)

    sleep(1)
    navegador.quit()
except Exception as error:
    print(error)
    navegador.quit()


