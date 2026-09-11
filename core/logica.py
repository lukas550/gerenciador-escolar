# Módulo para a lógica da aplicação, funções do CRUD.

"""
Funções:
1. Adicionar Aluno
2. Listar Aluno
3. Buscar Aluno
4. Excluir Aluno
5. Editar Aluno
6. Gerar Relatório
"""

# Funções do CRUD

def adicionar_aluno(nome, notas, descricao):
    # Validações
    if not nome.strip() or not descricao.strip():
        raise ValueError("Informações inválidas!")

    if len(notas) != 3:
        raise ValueError("Deve haver exatamente 3 notas!")

    if len(descricao) > 50 or len(descricao) < 3:
        raise ValueError("Descrição deve ter 3-50 caracteres!")

    for nota in notas:
        if nota < 0 or nota > 10:
            raise ValueError(f"A nota {nota} é inválida!")
        
    media = sum(notas) / 3
    situacao = True if media > 6 else False

    # Cria e retorna dicionário
    aluno_dicionario = {
        "nome": nome.lower().strip(),
        "notas": notas,
        "media": media,
        "situacao": situacao,
        "informacao": descricao.lower().strip()
    }

    return aluno_dicionario

def listar_alunos(sistema):
    # Validações
    if not isinstance(sistema, list):
        raise TypeError("Sistema deve ser uma lista.")

    if not sistema:
        raise TypeError("Sem alunos no sistema!")

    # Lista os alunos
    for aluno in sistema:
        situacao_do_aluno = "Aprovado" if aluno['situacao'] else "Reprovado"
        print(f"- {aluno['nome'].capitalize()} | Média: {aluno['media']:.2f} | {situacao_do_aluno} | {aluno['informacao']}")

def buscar_aluno(sistema, aluno_buscado):
    # Validações
    if not isinstance(sistema, list):
        raise TypeError("Sistema deve ser uma lista!")

    if not sistema or not aluno_buscado.strip():
        raise TypeError("As informações estão inválidas!")

    # Busca
    encontrado = False
    for aluno in sistema:
        if aluno["nome"] == aluno_buscado.lower().strip():
            encontrado = True
            aluno_achado = aluno
            break

    if not encontrado:
        raise TypeError(f"Aluno {aluno_buscado.capitalize()} não foi encontrado!")

    return aluno_achado

def excluir_aluno(sistema, aluno, confirmacao=False):
    # Validações
    if not isinstance(sistema, list):
        raise TypeError("Sistema deve ser uma lista!")

    if not sistema or not aluno.strip():
        raise TypeError("As informações estão inválidas!")

    if not confirmacao:
        raise TypeError("Operação cancelada.")

    # Exclusão
    sistema.remove(aluno)
    return aluno