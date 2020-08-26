from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of,
    invisibility_of_element
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
browser = Firefox()
browser.get(url)

wdw = WebDriverWait(browser, 30)

h1 = wdw.until(
    invisibility_of_element(browser.find_element_by_tag_name('h1')), 'h1 não foi encontrado na pagina, espera de  30 seg'
)

browser.quit()