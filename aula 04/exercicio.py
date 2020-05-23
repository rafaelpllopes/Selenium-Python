#! python3
from selenium.webdriver import Firefox
from time import sleep


"""
    Trabalhando com seletores css
    http://selenium.dunossauro.live/exercicio_05.html
    http://selenium.dunossauro.live/exercicio_06.html
    Zerar o https://flukeout.github.io
"""


def preenche_formulario(browser, formulario):
    nome = browser.find_element_by_css_selector(
        f".form-{formulario} input[name='nome']")
    senha = browser.find_element_by_css_selector(
        f".form-{formulario} input[name='senha']")
    enviar = browser.find_element_by_css_selector(
        f".form-{formulario} input[name='{formulario}']")
    sleep(0.5)
    nome.send_keys('nome')
    sleep(0.5)
    senha.send_keys('senha')
    sleep(0.5)
    enviar.click()


def exercicio_05(browser, url):
    browser.get(url)
    formulario_escolhido = ''
    while not formulario_escolhido == '... Mentira, você conseguiu terminar':
        sleep(5)
        formulario_escolhido = browser.find_element_by_css_selector(
            'header p span').text
        try:
            preenche_formulario(browser, formulario_escolhido)
        except:
            pass


def exercicio_06(browser, url):
    browser.get(url)
    formulario = ''

    while not formulario == '... Mentira, você conseguiu terminar':
        try:
            sleep(5)
            formulario = browser.find_element_by_css_selector(
                'header p:nth-child(2) span').text
            numero_da_vez = browser.find_element_by_css_selector('#num').text
            preenche_formulario(browser, formulario)
        except:
            pass


def main():
    url_exercicio05 = 'http://selenium.dunossauro.live/exercicio_05.html'
    url_exercicio06 = 'http://selenium.dunossauro.live/exercicio_06.html'

    firefox = Firefox()
    firefox.implicitly_wait(30)

    # exercicio_05(firefox, url_exercicio05)
    exercicio_06(firefox, url_exercicio06)

    try:
        sleep(5)
        firefox.quit()
    except:
        pass


if __name__ == '__main__':
    main()
