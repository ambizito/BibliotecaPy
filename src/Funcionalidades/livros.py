def carregar_livros(arquivo_db=r'F:\BibliotecaPy\src\livros_db.txt'):
    """
    Carrega os livros do arquivo de banco de dados especificado e retorna uma lista de dicionários.
    Cada dicionário contém informações sobre um livro, incluindo seu ID, nome, ID do autor, autor,
    gêneros (como lista) e data de lançamento.
    
    :param arquivo_db: O caminho para o arquivo de banco de dados dos livros.
    :return: Uma lista de dicionários, onde cada dicionário representa um livro.
    """
    livros = []
    try:
        with open(arquivo_db, 'r', encoding='utf-8') as file:
            for line in file:
                partes = line.strip().split(',')
                if len(partes) == 6:
                    livro_id, nome, autor_id, autor, generos, data_lancamento = partes
                    livros.append({
                        'livro_id': int(livro_id),
                        'nome': nome.strip(),
                        'autor_id': int(autor_id),
                        'autor': autor.strip(),
                        'generos': [genero.strip() for genero in generos.split('|')],
                        'data_lancamento': data_lancamento.strip()
                    })
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo_db}")
    except Exception as e:
        print(f"Erro ao carregar livros: {e}")
    
    return livros

def pesquisar_por_nome(livros, termo_pesquisa):
    """
    Filtra livros pelo termo de pesquisa no nome.
    
    :param livros: Lista de dicionários, onde cada dicionário representa um livro.
    :param termo_pesquisa: String que representa o termo de pesquisa inserido pelo usuário.
    :return: Lista de dicionários filtrados pelo termo de pesquisa no nome do livro.
    """
    termo_pesquisa = termo_pesquisa.lower().strip()
    livros_filtrados = [livro for livro in livros if termo_pesquisa in livro['nome'].lower()]
    return livros_filtrados

def mostrar_livros_paginados(livros, pagina=1, livros_por_pagina=10):
    total_livros = len(livros)
    total_paginas = (total_livros // livros_por_pagina) + (1 if total_livros % livros_por_pagina > 0 else 0)
    inicio = (pagina - 1) * livros_por_pagina
    fim = inicio + livros_por_pagina
    livros_pagina = livros[inicio:fim]

    print(f"Página {pagina}/{total_paginas}\n")
    for i, livro in enumerate(livros_pagina, start=inicio + 1):
        print(f"{i}. {livro['nome']}")

    return pagina, total_paginas

def interagir_com_usuario():
    livros = carregar_livros()  # Supõe uma lista de dicionários, cada um representando um livro
    pagina_atual = 1
    livros_por_pagina = 10

    while True:
        pagina_atual, total_paginas = mostrar_livros_paginados(livros, pagina_atual, livros_por_pagina)
        print("\nDigite o nome do livro para pesquisar ou 'P' para próxima página, 'A' para anterior, 'Q' para sair:")
        entrada = input().strip()

        if entrada.lower() == 'p':
            if pagina_atual < total_paginas:
                pagina_atual += 1
            else:
                print("Você já está na última página.")
        elif entrada.lower() == 'a':
            if pagina_atual > 1:
                pagina_atual -= 1
            else:
                print("Você já está na primeira página.")
        elif entrada.lower() == 'q':
            break
        else:
            livros_filtrados = pesquisar_por_nome(livros, entrada)
            if livros_filtrados:
                mostrar_livros_paginados(livros_filtrados, 1, len(livros_filtrados))
                input("Pressione Enter para voltar à lista completa.")
            else:
                print("Nenhum livro encontrado. Tente novamente.")
            pagina_atual = 1  # Retorna para a primeira página da lista completa
