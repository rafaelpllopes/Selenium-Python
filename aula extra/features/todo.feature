Funcionalidade: Todo List

    Cenário: Criar um cartão de Todo
        Dado que eu esteja na página
        Quando cria um todo
            """
                {
                    "nome": "Dormir",
                    "descricao": ["é bom"]
                }
            """
        Então o todo deve estar na pilha "A fazer"

    Cenário: Criar dois cartões de Todo
        Dado que eu esteja na página
        Quando cria os seguintes todos
            | nome | descricao |
            | Dormir | é bom |
            | Comer | Ao meio dia |

        Então o todo deve estar na pilha t "A fazer"
            | nome | descricao |
            | Dormir | é bom |