from selenium.webdriver import Firefox
from pages.pages import PageTodo

url = 'https://selenium.dunossauro.live/todo_list.html'
browser = Firefox()

"""
Cenário: Criar um cartão
    Dado que esteja na página de todo
    Quando criar um cartão
    Então o cartão deve estar na pilha "A fazer"
"""

# Dado que esteja na página de todo
print('Dado que esteja na página de todo')
todo_page = PageTodo(
    browser,
    url
)
todo_page.open()

# Quando criar um cartão
print('Quando criar um cartão')
todo_page.todo.create_todo(
    'POM',
    'POM POM'
)

# Então o cartão deve estar na pilha "A fazer"
print('Então o cartão deve estar na pilha "A fazer"')
primeiro_todo = todo_page.a_fazer.todos[0]
assert  primeiro_todo.name == 'POM'
assert primeiro_todo.description == 'POM POM'

browser.quit()

"""
    AAA - 3A
    - Arrange - Organizar
    - Act - Agir
    - Assert - Afirmar ou Garantir
"""