#! python3

from selenium.webdriver import Firefox
from urllib.parse import urlparse
from json import loads
from time import sleep

"""
    Desafio:
        - Preencher o formulario
        - Enviar dados do formulario
        - Pegar a url de resultado e fazer o assert da query
"""
firefox = Firefox()

url = 'http://selenium.dunossauro.live/exercicio_04.html'
firefox.get(url)
sleep(3)

def preencher_formulario(browser, nome, email, senha, telefone):
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

preencher_formulario(firefox, **estrutura)
sleep(2)

def gera_dicionario_da_query_http(current_url):
    """
        Gera dicionario atraves do http query
            - current_utl: url atual do site
    """
    # Pega a url
    url_content = urlparse(current_url)

    # Pega a query da url
    http_query = url_content.query

    # Separa os itens da query
    query_itens = http_query.split('&')

    # Inicia o dicionario 
    dicionario = {}

    # Percorre os itens da query para por no dicionario
    for item in query_itens:

        # Separa a chave e valor
        chave, valor = item.split('=')

        # Pega somente os itens necessarios
        if chave in ['nome', 'email', 'senha', 'telefone']:
            dicionario.update({
                chave: valor if chave != 'email' else valor.replace('%40', '@') # Operador ternario para reescrita do @ no email
            })
    
    return dicionario

dic_result = gera_dicionario_da_query_http(firefox.current_url)

# Verificar se os valores estão batendo
assert dic_result == estrutura

"""
    Compara resultado do http query, com o resultado na pagina
"""

def abrir_json(browser, tag):
    json_resultado = firefox.find_element_by_tag_name(tag).text
    resultado_arrumado = json_resultado.replace('\'', '\"')
    resultado = loads(resultado_arrumado)
    return resultado

resultado = abrir_json(firefox, 'textarea')

assert dic_result == resultado

firefox.quit()