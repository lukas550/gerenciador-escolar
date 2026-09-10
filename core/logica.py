# Módulo para a lógica da aplicação, funções do CRUD como: Adicionar alunos, Listar Alunos, Buscar aluno, Remover aluno, Editar aluno e também gera um relatório!

def adicionar_aluno(nome, notas, descricao):
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

    aluno_dicionario = {
        "nome": nome.lower().strip(),
        "notas": notas,
        "media": media,
        "situacao": situacao,
        "informacao": descricao.lower().strip()
    }

    return aluno_dicionario