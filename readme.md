# Gerenciador Escolar

Sistema de gerenciamento de alunos desenvolvido em Python, operado via terminal interativo.

---

## Sobre o Projeto

O Gerenciador Escolar é uma aplicação de linha de comando que permite registrar, consultar, editar e remover alunos de um sistema escolar. Cada aluno possui nome, informações descritivas, três notas individuais, média calculada automaticamente e situação acadêmica definida com base nessa média.

O projeto foi desenvolvido como exercício prático de consolidação dos fundamentos de Python, com foco na integração de estruturas de dados, funções, tratamento de erros e lógica de controle de fluxo.

---

## Como Funciona

Ao iniciar o programa, o menu principal é exibido no terminal. O usuário navega pelo sistema digitando o número correspondente à opção desejada. Todas as operações — cadastro, listagem, busca, remoção, edição e relatório — são executadas sobre uma lista em memória carregada a partir do arquivo `alunos.json`. Os dados são salvos automaticamente após cada operação que modifica o sistema.

A situação de cada aluno (aprovado ou reprovado) é calculada automaticamente com base na média das três notas, usando o critério de aprovação com média igual ou superior a 6.0.

---

## Funcionalidades

- **Adicionar Aluno** — Registra nome, informações descritivas e três notas. Calcula média e situação automaticamente.
- **Listar Alunos** — Exibe todos os alunos cadastrados com média e situação.
- **Buscar Aluno** — Localiza um aluno pelo nome e exibe seus dados completos.
- **Excluir Aluno** — Remove um aluno do sistema com confirmação obrigatória antes da exclusão.
- **Editar Aluno** — Permite editar notas, nome ou informações de um aluno individualmente via submenu.
- **Relatório Geral** — Exibe total de alunos, listas de aprovados e reprovados, maior e menor média, e média geral da turma.
- **Sair** — Encerra o programa com confirmação obrigatória.

---

## Como Executar

**Requisito:** Python 3.10 ou superior.

```bash
# Clone o repositório
git clone https://github.com/lukas550/gerenciador-escolar.git

# Acesse o diretório
cd gerenciador-escolar

# Execute o programa
python main.py
```

Nenhuma dependência externa é necessária. A aplicação utiliza apenas a biblioteca padrão do Python.

---

## Estrutura do Projeto

```
gerenciador-escolar/
│
├── main.py                  — Ponto de entrada; loop principal e interface com o usuário
│
└── core/
    ├── logica.py            — Funções de CRUD e relatório
    ├── armazenamento.py     — Leitura e escrita do arquivo alunos.json
    └── organizacao.py       — Utilitários de exibição (menu e linha decorativa)
```

**Responsabilidades por módulo:**

- `main.py` — Captura inputs, valida entradas do usuário, chama funções dos módulos e exibe resultados.
- `core/logica.py` — Contém `adicionar_aluno()`, `listar_alunos()`, `buscar_aluno()`, `excluir_aluno()`, `editar_aluno()` e `gerar_relatorio()`. Todas as funções validam os dados recebidos e lançam exceções em caso de erro.
- `core/armazenamento.py` — Contém `salvar_arquivo()` e `carregar_arquivo()`. Gerencia a persistência dos dados em `alunos.json` com tratamento de erros de I/O.
- `core/organizacao.py` — Contém `lin()` (linha separadora configurável) e `menu()` (exibe dicionário como menu numerado).

**Estrutura de dados de cada aluno:**

```python
{
    "nome": str,
    "notas": [float, float, float],
    "media": float,
    "situacao": bool,
    "informacao": str
}
```

Os alunos são armazenados em uma lista de dicionários, serializada em `alunos.json`.

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
- Operações com coleções: iteração, adição, remoção e acesso por índice
- Funções nativas: `len()`, `sum()`, `max()`, `min()`
- Módulo `json` da biblioteca padrão para persistência de dados
- Organização em pacote Python com módulos independentes por responsabilidade

---

## Autor

Desenvolvido por **Lukas** para fins de estudo e prática de Python.
Este projeto integra o portfólio de aprendizado independente com foco em desenvolvimento back-end.