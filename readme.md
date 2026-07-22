# Gerenciador Escolar

Sistema de gerenciamento de alunos desenvolvido em Python, operado via terminal interativo.

---

## Sobre o Projeto

O Gerenciador Escolar é uma aplicação de linha de comando que permite registrar, consultar, editar e remover alunos de um sistema escolar. Cada aluno possui nome, informações descritivas, três notas individuais, média calculada automaticamente e situação acadêmica definida com base nessa média.

O projeto foi desenvolvido como exercício prático de consolidação dos fundamentos de Python, com foco na integração de estruturas de dados, funções, tratamento de erros e lógica de controle de fluxo.

---

## Como Funciona

Ao iniciar o programa, o menu principal é exibido no terminal. O usuário navega pelo sistema digitando o número correspondente à opção desejada. Todas as operações — cadastro, listagem, busca, remoção, edição e relatório — são executadas sobre um dicionário em memória que representa o banco de dados da sessão.

A situação de cada aluno (aprovado ou reprovado) é calculada automaticamente com base na média das três notas, usando o critério de aprovação com média igual ou superior a 6.0.

---

## Funcionalidades

- **Cadastrar Aluno** — Registra nome, informações descritivas e três notas. Calcula média e situação automaticamente.
- **Listar Nomes** — Exibe todos os alunos cadastrados com média e situação.
- **Buscar Aluno** — Localiza um aluno pelo nome e exibe seus dados completos.
- **Remover Aluno** — Remove um aluno do sistema com confirmação obrigatória antes da exclusão.
- **Editar Aluno** — Permite editar notas, nome ou informações de um aluno individualmente.
- **Relatório Final** — Exibe total de alunos, listas de aprovados e reprovados, maior e menor média, e média geral da turma.
- **Sair** — Encerra o programa.

---

## Como Executar

**Requisito:** Python 3.10 ou superior (uso de f-strings com expressões aninhadas).

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/gerenciador-escolar.git

# Acesse o diretório
cd gerenciador-escolar

# Execute o programa
python gerenciadorescolar.py
```

Nenhuma dependência externa é necessária. A aplicação utiliza apenas a biblioteca padrão do Python.

---

## Estrutura do Código

```
gerenciadorescolar.py
│
├── Configuração inicial
│   ├── menu          — Tupla com as opções do menu principal
│   ├── edicoes       — Tupla com as opções do submenu de edição
│   └── sistema       — Dicionário principal que armazena todos os alunos
│
├── Funções utilitárias
│   ├── lin()         — Imprime uma linha separadora configurável
│   └── opcoes()      — Exibe o menu principal ou o submenu de edição
│
├── Funções de operação
│   ├── cadastrar_aluno()   — Coleta e valida dados; registra no dicionário
│   ├── listar_nomes()      — Itera sobre o dicionário e exibe resumo dos alunos
│   ├── buscar_alunos()     — Busca por chave no dicionário e exibe dados completos
│   ├── remover_aluno()     — Remove entrada do dicionário com confirmação
│   ├── editar_aluno()      — Submenu para edição parcial dos dados de um aluno
│   └── relatorio_final()   — Agrega e exibe estatísticas gerais do sistema
│
└── Loop principal
    └── while True    — Controla a navegação entre as opções do menu
```

**Estrutura de dados de cada aluno:**

```python
sistema = {
    "nome_do_aluno": {
        "notas": [nota1, nota2, nota3],
        "media": float,
        "situacao": "aprovado" | "reprovado",
        "informacao": str
    }
}
```

---

## Futuras Alterações

As melhorias planejadas para as próximas versões incluem:

- **Persistência em arquivo `.txt`** — Salvar e carregar os dados do sistema em arquivos de texto simples, permitindo que as informações sejam mantidas entre sessões.
- **Persistência em arquivo `.json`** — Serializar o dicionário `sistema` em formato JSON, oferecendo uma solução mais estruturada e adequada para integração futura com outras ferramentas.

Ambas as implementações exigirão o uso do módulo `json` da biblioteca padrão do Python e o tratamento de erros relacionados a leitura e escrita de arquivos.

---

## Tecnologias Utilizadas

**Linguagem:**
- Python 3.10+

**Fundamentos aplicados:**
- Tipos de dados: strings, floats, listas, tuplas e dicionários
- Funções com parâmetros e retorno
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while`, `for`)
- Tratamento de erros com `try`, `except`, `else` e `raise`
- Métodos de string: `.lower()`, `.strip()`, `.capitalize()`, `.join()`
- Operações com coleções: iteração, adição, remoção e acesso por chave
- Funções nativas: `len()`, `sum()`, `max()`, `min()`, `enumerate()`

---

## Autor

Desenvolvido por **Lukas** para fins de estudo e prática de Python.
Este projeto integra o portfólio de aprendizado independente com foco em desenvolvimento back-end.