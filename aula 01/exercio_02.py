#! python3.8.2
from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

navegador = Firefox()
try:
    navegador.get(url)
    sleep(1)
    p = navegador.find_elements_by_tag_name('p')
    [esperado_texto, numero_esperado] = p[1].text.split(':')
    botao = navegador.find_element_by_id('ancora')
    
    valor_atual_p = ''
    
    while f'Você ganhou:{numero_esperado}' != valor_atual_p:
        botao.click()
        p = navegador.find_elements_by_tag_name('p')
        valor_atual_p = p[-1].text

        print(valor_atual_p)

    sleep(10)
    navegador.quit()

except Exception as error:
    print(error)
    navegador.quit()


