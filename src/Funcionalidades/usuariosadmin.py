from utils import clear_terminal


def sair():
    clear_terminal()
    return False

def entrar_como_admin(admin_password):
    while True:
        password = input("Digite a senha do administrador (para sair digite '..'): ")
        if password == "..":
            return False
        elif password == admin_password:
            clear_terminal()
            print("Você agora está logado como administrador.")
            return True
        else:
            print("Senha incorreta.")