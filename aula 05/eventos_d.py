#! python3
from selenium.webdriver import Firefox
from time import sleep

"""
    Eventos: Focus, Blur, change
    Focus: quando o elemento é acessado está com foco;
    Blur: quando o elemento perde o foco.
    Change: é um evento de mudança, que pode ativar após o elemento perder o foco;
"""

browser = Firefox()
browser.implicitly_wait(30)
url = 'http://selenium.dunossauro.live/aula_07_d.html'

"""
    1. Checar se a mudança ocorre no span (focus, blur) - OK
    2. Checar se a mudança ocorre no p (chage)
"""

browser.get(url)
input_de_texto = browser.find_element_by_name('nome')
span = browser.find_element_by_tag_name('span')
p = browser.find_element_by_tag_name('p')

"""
    Quando clicar no elemento 'input'
    Então o texto 'está com foco' deve ser o content de 'span'
    Quando clicar no elemento 'span'
    Então o texo 'esta sem foco' deve ser o content de 'span'
"""

input_de_texto.click()
assert 'está com foco' == span.text, 'Está com foco não esta em span'
print(span.text)

span.click()
assert 'está sem foco' == span.text, 'Está sem foco não esta em span'
print(span.text)

"""
    Dado que o texto '0' deser o content de 'p'
    Quando enviar "batata" no elemento 'input'
    Então o texto 'está com foco' deve ser o content de 'span'
    Quando clicar no elemento 'span'
    Então o texo 'esta sem foco' deve ser o content de 'span'
    Então o texto '1' deve ser o valor de 'p'
"""

assert '0' == p.text, 'Valor 0 deve estar em p'
print(p.text)

texto = 'batata batatão batatinha'

# Simulando uma pessoal digitando rapido
for letra in texto:
    sleep(0.2)
    input_de_texto.send_keys(letra)

assert 'está com foco' == span.text, 'Está com foco não esta em span'
print(span.text)

span.click()
assert 'está sem foco' == span.text, 'Está sem foco não esta em span'
print(span.text)

assert '1' == p.text, 'Valor 1 deve estar em p'
print(p.text)

browser.quit()
