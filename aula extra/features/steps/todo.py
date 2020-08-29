# -*- coding: UTF-8 -*-
from behave import given, when, then
from json import loads
from todo_project.pages.pages import PageTodo

@given('que eu esteja na página')
def go_to_page(context):
    context.page = PageTodo(context.browser, 'https://selenium.dunossauro.live/todo_list.html')
    context.page.open()

@when('cria um todo')
def create_todo(context):
    texto_do_step = loads(context.text)
    context.page.todo.create_todo(
        name=texto_do_step['nome'],
        description=texto_do_step['descricao']
    )

@when('cria os seguintes todos')
def create_many_todo(context):
    for l in context.table.rows:
        linha_convertida = dict(l.items())
    
    context.page.todo.create_todo(
        name=linha_convertida['nome'],
        description=linha_convertida['descricao']
    )

@then('o todo deve estar na pilha "{elemento}"')
def check_todo(context, elemento):
    elemento = elemento.lower().replace(' ','_')
    page_element = getattr(context.page, elemento)
    assert 1 == len(page_element.todos)

@then('o todo deve estar na pilha t "{elemento}"')
def check_todos(context, elemento):
    elemento = elemento.lower().replace(' ','_')
    page_element = getattr(context.page, elemento)
    table_value = dict(context.table.rows[0].items())
    page_element.todos[0].name == table_value['nome']
    