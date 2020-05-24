#! python3

from selenium.webdriver import Firefox
from urllib.parse import urlparse, parse_qsl
from json import loads
from time import sleep

"""
    Desafio:
        - Preencher o formulario
        - Enviar dados do formulario
        - Pegar a url de resultado e fazer o assert da query
"""
firefox = Firefox()
firefox.implicitly_wait(30)

url = 'http://selenium.dunossauro.live/exercicio_04.html'
firefox.get(url)

# ---- Parte 1

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

def gera_dicionario_da_query_http(current_url):
    """
        Gera dicionario atraves do http query
            - current_utl: url atual do site
    """

    """
        Forma 1: utilizando urlparser
    """
    # # Pega a url
    # url_content = urlparse(current_url)

    # # Pega a query da url
    # http_query = url_content.query

    # # Separa os itens da query
    # query_itens = http_query.split('&')

    # # Inicia o dicionario 
    # dicionario = {}

    # # Percorre os itens da query para por no dicionario
    # for item in query_itens:

    #     # Separa a chave e valor
    #     chave, valor = item.split('=')

    #     # Pega somente os itens necessarios
    #     if chave in ['nome', 'email', 'senha', 'telefone']:
    #         dicionario.update({
    #             chave: valor if chave != 'email' else valor.replace('%40', '@') # Operador ternario para reescrita do @ no email
    #         })

    """
        Forma 2: Utilizando parser_qsl do urllib para gerar o parser da query
    """

    dicionario = dict(parse_qsl(urlparse(current_url).query))
    dicionario.pop('btn')
    
    return dicionario

dic_result = gera_dicionario_da_query_http(firefox.current_url)

# Verificar se os valores estão batendo
print(f'Teste 1 passou: {"sim" if dic_result == estrutura else "não" }')
assert dic_result == estrutura

# ---- Parte 2

"""
    Compara resultado do http query, com o resultado na pagina
"""

# Forma 1 - Não recomendado usar
# Utilizando eval
# resultado = eval(firefox.find_element_by_tag_name('textarea').text)

# Forma 2
# Utilizando json - FORMA MAIS CORRETA
def abrir_json(browser, tag):
    json_resultado = firefox.find_element_by_tag_name(tag).text
    resultado_arrumado = json_resultado.replace('\'', '\"')
    resultado = loads(resultado_arrumado)
    return resultado

resultado = abrir_json(firefox, 'textarea')

print(f'Teste 2 passou: {"sim" if dic_result == resultado else "não"}')
assert dic_result == resultado

firefox.quit()