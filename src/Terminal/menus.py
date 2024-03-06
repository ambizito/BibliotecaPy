import os
from Funcionalidades.livros import procurar_livros, procurar_autor, generos, data_de_publicacao
from Funcionalidades.usuarios import cadastrar, remover, editar, sair

"""
Este módulo contém funções relacionadas aos menus do terminal.
"""


def clear_terminal():
    """
    Limpa a tela do terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """
    Imprime as opções do menu e lida com a entrada do usuário.
    """
    options = [
        ("Procurar livros", procurar_livros),
        ("Procurar Autor", procurar_autor),
        ("Gêneros", generos),
        ("Data de Publicação", data_de_publicacao),
        ("Cadastrar", cadastrar),
        ("Remover", remover),
        ("Editar", editar),
        ("Sair", sair)
    ]
    clear_terminal()
    print("O que você gostaria de fazer hoje?")
    for i, (option, _) in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            user_input = int(input("Digite o número da opção desejada: "))  # Solicita ao usuário que digite o número da opção desejada
            if user_input < 1 or user_input > len(options):  # Verifica se o número digitado é válido
                raise ValueError(
                    "Opção inválida. Por favor, digite um número de 1 a "
                    f"{len(options)}."
                )
            break
        except ValueError as e:
            print(str(e))  # Exibe a mensagem de erro caso o valor digitado não seja um número
    options[user_input - 1][1]()  # Chama a função correspondente à opção selecionada

    # End-of-file (EOF)
