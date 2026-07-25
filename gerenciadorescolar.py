menu_de_opcoes = {
    "1": "Cadastrar Aluno",
    "2": "Listar Nomes",
    "3": "Buscar Aluno",
    "4": "Remover Aluno",
    "5": "Editar Aluno",
    "6": "Relátorio Final",
    "7": "Sair"
}
menu_de_edicoes = {
    "1": "Editar notas",
    "2": "Editar nome",
    "3": "Editar informações",
    "4": "Sair"
}
sistema = {

}

"""
Estrutura dos dados:
nome = {
    notas = [],
    media = float,
    situacao = string (aprovado ou reprovado),
    infromacao = string,
}
"""

# Funções organizadoras e estruturais
def lin(char, qtd=30):
    return print(char * qtd)

def opcoes(tabela=False, edicao=False):

    if tabela:
        for nu, opcao in menu_de_opcoes.items():
            print(f'{nu}. {opcao}')
    elif edicao:
        for nu, edit in menu_de_edicoes.items():
            print(f'{nu}. {edit}')
    else:
        return

def pedir_notas():
    lista = []
    while len(lista) < 3:
        try:
            nota = float(input(f'Digite a nota {len(lista) + 1} do aluno: '))
            if nota < 0 or nota > 10:
                raise ValueError
        except ValueError:
            print('Digite um valor válido!')
            continue
        else:
            lista.append(nota)
    return lista

def pedir_informacoes():
    while True:
        informacoes = input('Digite sobre o aluno (MAX 50): ')
        if len(informacoes) > 50 or len(informacoes) < 3:
            print('Tente novamente!')
            continue
        else:
            break
    return informacoes

# Funções de Features
def cadastrar_aluno():

    nome_do_aluno = input('Digite o nome do aluno: ').lower().strip()
    if nome_do_aluno in sistema:
        print("\nNome já registrado!\n")
        return
    informacao_do_aluno = pedir_informacoes()
    print()
    lista_das_notas = pedir_notas()
    print('\nCadastro Finalizado!\n')

    media_do_aluno = sum(lista_das_notas) / 3
    situacao_do_aluno = "aprovado" if media_do_aluno >= 6 else "reprovado"

    sistema[nome_do_aluno] = {
        'notas': lista_das_notas,
        'media': media_do_aluno,
        'situacao': situacao_do_aluno,
        'informacao': informacao_do_aluno
    }

def listar_nomes():
    if not sistema:
        print('Sem alunos no sistema!')
    else:
        lin('*')
        for nome, informacao in sistema.items():
            print(f"Nome: {nome.capitalize()} / Média: {informacao['media']:.2f} / Situação: {informacao['situacao']}")
        lin('*')

def buscar_alunos():
    if not sistema:
        print('Sem alunos no sistema!')
    else:
        busca = input('Digite o nome do aluno que procura: ').lower()
        if busca in sistema:
            dados = sistema[busca]
            print(f"Nome: {busca.capitalize()}")
            notas_formatadas = ', '.join(f'{n:.1f}' for n in dados['notas'])
            print(f"Notas: {notas_formatadas}")
            print(f"Média: {dados['media']:.2f}")
            print(f"Situação: {dados['situacao']}")
            print(f"Informações: {dados['informacao']}")
        else:
            print('Aluno não encontrado!')

def remover_aluno():
    if not sistema:
        print('Sem alunos no sistema!')
    else:
        deletar = input('Digite o aluno pra deletar do sistema: ').lower().strip()
        if deletar in sistema:
            while True:
                entrada = input('Tem certeza? Essa ação é irreversível. (SIM/NÃO): ').lower().strip()
                if entrada in ["sim", "s"]:
                    del sistema[deletar]
                    print('Deletado!')
                    break
                elif entrada in ["não", "nao", "n"]:
                    print('Não deletado!')
                    break
                else:
                    print('Digite algo válido!')
                    continue
        else:
            print('Nome não encontrado!')

def editar_aluno():
    lin('*')
    if not sistema:
        print('Sem alunos no sistema!')
    else:
        busca = input('Digite o nome do aluno que busca editar: ').lower().strip()
        if busca in sistema:
            dados = sistema[busca]
            opcoes(False, True)
            print('Digite "edição" para ver as opções;')

            while True:
                escolha = input('= ').lower().strip()
                if escolha == 'edição' or escolha == 'edicao':
                    lin('-')
                    opcoes(False, True)
                    lin('-')
                elif escolha == '1':
                    novas_notas = pedir_notas()
                    dados["notas"] = novas_notas
                    dados["media"] = sum(novas_notas) / 3
                    dados["situacao"] = "aprovado" if dados["media"] >= 6 else "reprovado"
                    print("\nNotas alteradas com sucesso!\n")
                elif escolha == '2':
                        novo_nome = input('Digite o novo nome: ').lower().strip()
                        sistema[novo_nome] = sistema.pop(busca)
                        dados = sistema[novo_nome]
                        busca = novo_nome
                        print('\nNome atualizado!\n')
                elif escolha == '3':
                    novas_informacoes = pedir_informacoes()
                    dados['informacao'] = novas_informacoes
                    print("\nInformações atualizadas!\n")
                elif escolha == '4':
                    print('\nEncerrando edições...\n')
                    break
                else:
                    print('Digite uma opção válida!')
    lin('*')

def relatorio_final():
    if not sistema:
        print('Sem dados de aluno no sistema!')
    else:
        print(f'1. Total de Alunos: {len(sistema)}')
        print('2. Lista de aprovados e reprovados:')
        print('AP:')
        for nome in sistema.keys():
            if (sistema[nome]['situacao']) == 'aprovado':
                print(f'- {nome.capitalize()}')
        print('REP:')
        for nome in sistema.keys():
            if (sistema[nome]['situacao']) == 'reprovado':
                print(f'- {nome.capitalize()}')
        medias = []
        for dados in sistema.values():
            medias.append(dados['media'])
        maior = max(medias)
        menor = min(medias)
        print(f'3. Maior Média: {maior:.2f} / Menor Média: {menor:.2f}')
        print(f'4. Média da turma: {sum(medias) / len(sistema):.2f}')


# Principal:
opcoes(True, False)
print('Digite o comando "opção" para ver as opções novamente!')
while True:
    print()
    escolha = input('= ').lower()
    print()
    if escolha == 'opção' or escolha == "opcao":

        lin('-')
        opcoes(True, False)
        lin('-')

    elif escolha == '1':

        lin('-')
        cadastrar_aluno()
        lin('-')

    elif escolha == '2':

        lin('-')
        listar_nomes()
        lin('-')

    elif escolha == '3':

        lin('-')
        buscar_alunos()
        lin('-')

    elif escolha == '4':

        lin('-')
        remover_aluno()
        lin('-')

    elif escolha == '5':
        
        lin('-')
        editar_aluno()
        lin('-')

    elif escolha == '6':

        lin('-')
        relatorio_final()
        lin('-')

    elif escolha == '7':
        print('\nEncerrando...\n')
        break
    else:
        print('Opção inválida!')
print('Obrigado por testar! :DD')