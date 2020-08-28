"""
    DSL

    Página:
        - Barra de navegação
        - Todo
            - Nome
            - Descrição
            - Urgente
            - Botão
            * Criar todo
                & nome
                & descrição
                & urgente
                & clique
        - A fazer
            - Cartões
        - Fazendo
            - Cartões
        - Pronto
            - Cartões
        - Cartão
            - Nome/Titulo
            - Descrição
            - Botão pronto
            - Botão cancelar
        
"""
from abc import ABC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PageElement(ABC):
    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url
    
    def open(self):
        self.webdriver.get(self.url)

    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)

class Todo(PageElement):
    """
        atributo = locator.
    """    
    name = (By.ID, 'todo-name')
    description = (By.ID, 'todo-desc')
    urgent = (By.ID, 'todo-next')
    submit = (By.ID, 'todo-submit')


    def create_todo(self, name, description, urgent=False):
        self.webdriver.find_element(*self.name).send_keys(name)
        self.webdriver.find_element(*self.description).send_keys(description)
        if urgent:
            self.webdriver.find_element(*self.urgent).click()
        self.webdriver.find_element(*self.submit).click()

class CardContainer(PageElement, ABC):
    def todos(self):
        fieldset = self.find_element(self.fieldset)
        cards = fieldset.find_elements(*self.card)
        return [Card(card) for card in cards]
        # po_cards = []
        # for card in cards:
        #     po_cards.append(Card(card))
        # return po_cards

class AFazer(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_a fieldset')
    card = (By.CLASS_NAME, 'terminal-card')

class Fazendo(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_b fieldset')
    card = (By.CLASS_NAME, 'terminal-card')

class Pronto(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_c fieldset')
    card = (By.CLASS_NAME, 'terminal-card')

class Card:
    def __init__(self, selenium_object):
        self.selenium_object = selenium_object
        self.name = (By.CSS_SELECTOR, 'header.name')
        self.description = (By.CSS_SELECTOR, 'div.description')
        self._do = By.CSS_SELECTOR, 'button.do'
        self._cancel = By.CSS_SELECTOR, 'button.cancel'
        self._load()

    def do(self):
        self.selenium_object.find_element(*self._do).click()
    
    def cancel(self):
        try:
            self.selenium_object.find_element(*self._cancel).click()
        except NoSuchElementException:
            print('Elemento não tem cancelar')

    def _load(self):
        self.name = self.selenium_object.find_element(*self.name).text
        self.description = self.selenium_object.find_element(*self.description).text
    
    def __repr__(self):
        return f'Card(name="{self.name}", description="{self.description}")'

def main():
    from selenium.webdriver import Firefox
    from time import sleep
    webdriver = Firefox()
    url = 'https://selenium.dunossauro.live/todo_list.html'

    todo_element = Todo(webdriver, url)
    todo_element.open()
    todo_element.create_todo(
        name='teste1',
        description='teste1'
    )

    todo_element.create_todo(
        name='teste2',
        description='teste2'
    )

    a_fazer = AFazer(webdriver)
    tasks = a_fazer.todos()
    print(f'a fazer: {a_fazer.todos()}')
    tasks[0].do()

    fazendo = Fazendo(webdriver)
    print(f'fazendo: {fazendo.todos()}')
    tasks[0].do()

    pronto = Pronto(webdriver)
    print(f'pronto: {pronto.todos()}')

    tasks[1].do()
    tasks[1].do()
    
    print(f'a fazer: {a_fazer.todos()}')

    tasks[0].do()
    print(f'a fazer: {a_fazer.todos()}')

if __name__ == '__main__':
    main()