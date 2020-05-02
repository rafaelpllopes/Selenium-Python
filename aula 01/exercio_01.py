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
    
    dicionario = { h1.text : 
        {
            p[0].get_attribute('atributo') : p[0].text,
            p[1].get_attribute('atributo') : p[1].text,
            p[2].get_attribute('atributo'): p[2].text
        }
    }
    
    print(dicionario)
    sleep(1)
    navegador.quit()
except Exception as error:
    print(error)
    navegador.quit()


