#! python3.8.2
from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Firefox()
try:
    navegador.get(url)
    sleep(0.5) # Aguardar o carregamento da pagina
    for click in range(10):
        ancora = navegador.find_element_by_id('ancora')
        texto = navegador.find_elements_by_tag_name('p')
        print(f'{ancora.text} executou e o valor do texto é {texto[-1].text}, o valor do click é {click}')
        print(f'Os valores são iguais {"sim" if texto[-1].text == str(click) else "não"}')
        ancora.click()
        sleep(0.5)
    sleep(1)
    navegador.quit()
except Exception as error:
    print(error)
    navegador.quit()


