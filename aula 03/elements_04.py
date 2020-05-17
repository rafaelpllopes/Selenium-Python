#! python3

from selenium.webdriver import Firefox
from urllib.parse import urlparse
from json import loads
from time import sleep

firefox = Firefox()

url_base = 'http://selenium.dunossauro.live'

"""
    Preencher formularios e enviar
"""
firefox.get(f'{url_base}/aula_05.html')
sleep(2)

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

estrutura = {
    'nome': 'teste', 
    'email': 'teste@teste.testes',
    'senha': 'senha',
    'telefone': '9999999'
}

# preenche_form(firefox, 'teste', 'teste@teste.testes', 'senha', '9999999')
preenche_form(firefox, **estrutura)

sleep(2)
current_url = urlparse(firefox.current_url)

texto_resultado = firefox.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', '\"')
dic_result = loads(resultado_arrumado)

assert dic_result == estrutura

sleep(3)
firefox.quit()