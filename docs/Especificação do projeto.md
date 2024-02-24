## Requisitosas de segurança para conexão segura ao banco de dados
Boas práticas de programação

As tabelas que se seguem apresentam os requisitos funcionais e não funcionais que detalham o escopo do projeto. Para determinar a prioridade de requisitos, aplicar uma técnica de priorização de requisitos e detalhar como a técnica foi aplicada.

### Requisitos Funcionais

| ID     | Descrição do Requisito                                                                                      | Prioridade |
|--------|-------------------------------------------------------------------------------------------------------------|------------|
|RF-001  | O sistema deve permitir o cadastro de livros contendo Autor, Título, Data de Publicação e Gênero.         | ALTA       |
|RF-002  | O sistema deve permitir remover livros.                                                                    | ALTA       |
|RF-003  | O sistema deve permitir alterar as informações dos livros.                                                 | ALTA       |
|RF-004  | O sistema deve permitir consultar livros por Autor, Título, Data de Publicação e Gênero.                  | ALTA       |
|RF-005  | O sistema deve suportar a paginação nos resultados das consultas.                                          | MÉDIA      |
|RF-006  | O sistema deve permitir a visualização de todos os livros cadastrados.                                     | MÉDIA      |
|RF-007  | O sistema deve validar os dados de entrada para cadastro e atualização de livros.                         | ALTA       |
|RF-008  | O sistema deve fornecer mensagens de erro claras para entradas inválidas ou operações não permitidas.     | ALTA       |
|RF-009  | O sistema deve suportar múltiplos usuários com diferentes níveis de acesso (admin, usuário comum).        | MÉDIA      |
|RF-010  | O sistema deve permitir a configuração de conexão ao banco de dados MySQL através de um arquivo de configuração. | ALTA |


### Requisitos Não Funcionais

| ID     | Descrição do Requisito                                                                                               | Prioridade |
|--------|----------------------------------------------------------------------------------------------------------------------|------------|
|RNF-001 | O sistema deve ser desenvolvido na linguagem Python, compatível com a versão 3.8 ou superior.                       | ALTA       |
|RNF-002 | O sistema deve utilizar o MySQL como sistema de gerenciamento de banco de dados.                                    | ALTA       |
|RNF-003 | A interface de linha de comando (CLI) deve ser intuitiva e fácil de usar, com comandos claros e opções de ajuda.   | ALTA       |
|RNF-004 | O sistema deve garantir a segurança dos dados, utilizando práticas recomendadas de conexão segura ao banco de dados. | ALTA       |
|RNF-005 | O sistema deve operar eficientemente, com tempos de resposta rápidos para as operações de cadastro, consulta, atualização e remoção de livros. | ALTA |
|RNF-006 | O sistema deve ser capaz de suportar pelo menos 1000 registros de livros sem degradação significativa do desempenho. | MÉDIA      |
|RNF-007 | O sistema deve ser documentado, incluindo documentação do código-fonte e manual do usuário.                         | ALTA       |
|RNF-008 | O sistema deve ser desenvolvido seguindo as boas práticas de programação, incluindo modularidade e reusabilidade do código. | ALTA       |
|RNF-009 | O sistema deve ser testável, com testes unitários e de integração cobrindo as principais funcionalidades.           | ALTA       |
|RNF-010 | O sistema deve ser facilmente configurável, permitindo a configuração de parâmetros como detalhes de conexão ao banco de dados através de arquivos de configuração externos. | ALTA |
|RNF-011 | O sistema deve oferecer suporte para internacionalização (i18n), permitindo fácil tradução para outros idiomas.     | BAIXA      |
|RNF-012 | O sistema deve ser implementado com uma arquitetura que permita futuras expansões e integrações.                     | MÉDIA      |
|RNF-013 | O sistema deve ser compatível com sistemas operacionais Windows, Linux e MacOS.                                     | MÉDIA      |
|RNF-014 | O sistema deve adotar uma licença de software aberto, permitindo uso, modificação e distribuição.                   | BAIXA      |
|RNF-015 | O sistema deve ser projetado para permitir a execução em ambientes de baixo recurso, como hardware limitado ou redes com baixa largura de banda. | BAIXA |
