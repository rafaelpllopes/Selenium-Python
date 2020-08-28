from selenium.webdriver import Firefox
from pages.pages import PageTodo

url = 'https://selenium.dunossauro.live/todo_list.html'
browser = Firefox()

# Arange ------------------------

todo_page = PageTodo(
    browser,
    url
)
todo_page.open()

# Act ------------------------
todo_page.todo.create_todo(
    'POM',
    'POM POM'
)

# Assert ------------------------
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