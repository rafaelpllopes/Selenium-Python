from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import (
    ActionChains
)
from selenium.webdriver.common.keys import Keys

url = 'https://selenium.dunossauro.live/caixinha'
browser = Firefox()
browser.implicitly_wait(30)
browser.get(url)

caixa = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span')

ac = ActionChains(browser)

def caixinha_colorida(*keys):
    if keys != None:
        for key in keys:
            ac.key_down(key)

    ac.move_to_element(caixa)
    ac.pause(1)
    ac.click(caixa)
    ac.pause(1)
    ac.double_click(caixa)
    ac.pause(1)
    ac.move_to_element(span)

    if keys != None:
        for key in keys:
            ac.key_up(key)

caixinha_colorida()
caixinha_colorida(Keys.SHIFT)
caixinha_colorida(Keys.CONTROL)
caixinha_colorida(Keys.SHIFT, Keys.CONTROL)

ac.move_to_element(caixa)
ac.pause(1)
ac.context_click(caixa)
ac.perform()
