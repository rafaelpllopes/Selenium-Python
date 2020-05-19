#! python3
from selenium.webdriver import Firefox
from time import sleep


"""
    Trabalhando com seletores css
        Operador    Significado
            =       Deve ser exatamene igual
            *=      Deve Ocorrer em
            |=      Deve ser exatamente ou iniciar
            ^=      Iniciado em
            $=      Terminado em
            ~=      Um deve ser exatamente igual
"""

url = 'http://selenium.dunossauro.live/aula_06_a.html'

firefox = Firefox()

firefox.get(url)
sleep(2)

"""
    Selecionando usando atributo type [attr=valor]
"""
nome = firefox.find_element_by_css_selector('[type="text"]')
senha = firefox.find_element_by_css_selector('[type="password"]')
btn = firefox.find_element_by_css_selector('[type="submit"]')
print(nome, senha, btn)

"""
    Selecionando usando atributo name [attr=valor]
"""
nome = firefox.find_element_by_css_selector('[name="nome"]')
senha = firefox.find_element_by_css_selector('[name="senha"]')
btn = firefox.find_element_by_css_selector('[name="l0c0"]')
print(nome, senha, btn)

"""
    Selecionando usando [attr*=valor]
"""
nome = firefox.find_element_by_css_selector('[name*="ome"]')
senha = firefox.find_element_by_css_selector('[name*="ha"]')
btn = firefox.find_element_by_css_selector('[name*="l0"]')
print(nome, senha, btn)

"""
    Operador    ação
                Seletores descemdemtes " div p"
        +       Selecionar irmão adjacente "div + p"
        >       seletores filho 

"""

elementos = firefox.find_elements_by_css_selector('div.form-group + br')
print(elementos[0])

nome.send_keys('nome')
senha.send_keys('senha')
btn.click()

sleep(3)
firefox.quit()