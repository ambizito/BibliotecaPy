import os
from Funcionalidades.livros import procurar_livros, procurar_autor, generos, data_de_publicacao
from Funcionalidades.usuarios import cadastrar, remover, editar, sair

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
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
            user_input = int(input("Digite o número da opção desejada: "))
            if user_input < 1 or user_input > len(options):
                raise ValueError(f"Opção inválida. Por favor, digite um número de 1 a {len(options)}.")
            break
        except ValueError as e:
            print(str(e))
    options[user_input - 1][1]()  # Call the corresponding function
