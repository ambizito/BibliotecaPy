from Funcionalidades.livros import interagir_com_usuario
from Funcionalidades.usuariosadmin import  sair, entrar_como_admin

userstate = False
admin_password = "123"

def print_menu():
    """
    Este módulo contém funções relacionadas aos menus do terminal.
    Imprime as opções do menu e lida com a entrada do usuário.
    """

    admin_options = [
        ("Procurar livros", interagir_com_usuario),
        ("Sair", sair),  # Remova os parênteses para passar a função, não o resultado da função
        ("Entrar como Admin", lambda: entrar_como_admin(admin_password))  # Use a variável admin_password, não a string "admin_password"
    ]
    user_options = [
        ("Procurar livros", interagir_com_usuario),
    ]
    

    while True:
        print("O que você gostaria de fazer hoje?")
        options = admin_options if userstate else user_options
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

        if options[user_input - 1][0] == "Sair":
            userstate.is_admin = sair()
        elif options[user_input - 1][0] == "Entrar como Admin":
            userstate.is_admin = entrar_como_admin(admin_password)
        else:
            options[user_input - 1][1]()  # Chama a função correspondente à opção selecionada

    # End-of-file (EOF)
