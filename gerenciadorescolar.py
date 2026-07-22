print('\nPROJETO 3; Gerenciador Escolar\n') # STATUS: completo / TODO: nenhuma
menu = ('Cadastrar Aluno', 'Listar Nomes', 'Buscar Alunos', 'Remover Aluno', 'Editar Aluno', 'Relátorio Final', 'Sair') # 1, 2, 3, 4, 5, 6, 7
edicoes = ('Editar notas', 'Editar nome', 'Editar Informações', 'Encerrar Ediçoes') # 1, 2, 3, 4
sistema = {

}

def lin(char, qtd=30):
    return print(char * qtd)

def opcoes(tabela=False, edicao=False):
    if tabela == True:
        for i, opcao in enumerate(menu, 1):
            print(f'{i}. {opcao}')
    elif edicao == True:
        for i, edit in enumerate(edicoes, 1):
            print(f'{i}. {edit}')
    else:
        return

def cadastrar_aluno():
    nome_do_aluno = input('Digite o nome do aluno: ').lower().strip()
    while True:
        informacoes = input('Digite sobre o aluno (MAX 50): ')
        if len(informacoes) > 50 or len(informacoes) < 3:
            print('Tente novamente!')
            continue
        else:
            break
    lista_das_notas = []
    while len(lista_das_notas) < 3:
        try:
            nota = float(input(f'Digite a nota {len(lista_das_notas) + 1} do aluno: '))
            if nota < 0 or nota > 10:
                raise ValueError
        except ValueError:
            print('Digite um valor válido!')
            continue
        else:
            lista_das_notas.append(nota)
    print('\nCadastro Finalizado!\n')
    notas_formatadas = ', '.join(str(nota) for nota in lista_das_notas)
    media_do_aluno = sum(lista_das_notas) / 3
    if media_do_aluno >= 6:
        situacao_do_aluno = 'aprovado'
    else:
        situacao_do_aluno = 'reprovado'
    sistema[nome_do_aluno] = {
        'notas': lista_das_notas,
        'media': media_do_aluno,
        'situacao': situacao_do_aluno,
        'informacao': informacoes
    }

def listar_nomes():
    if not sistema:
        print('Sem alunos no sistema!')
    else:
        lin('*')
        for nome, informacao in sistema.items():
            print(f'Nome: {nome.capitalize()} / Média: {informacao['media']} / Situação: {informacao['situacao']}')
        lin('*')

def buscar_alunos():
    if not sistema:
        print('Sem alunos no sistema!')
    else:
        busca = input('Digite o nome do aluno que procura: ').lower()
        if busca in sistema:
            dados = sistema[busca]
            print(f'Nome: {busca}')
            notas_formatadas = ', '.join(str(n) for n in dados['notas'])
            print(f'Notas: {notas_formatadas}')
            print(f'Média: {dados['media']}')
            print(f'Situação: {dados['situacao']}')
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
                if entrada == 'sim':
                    del sistema[deletar]
                    print('Deletado!')
                    break
                elif entrada == 'não' or entrada == 'nao':
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
        busca = input('Digite o nome do aluno que busca editar: ').lower()
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
                    lista_das_notas = []
                    while len(lista_das_notas) < 3:
                        try:
                            nota = float(input(f'Digite a nota {len(lista_das_notas) + 1} do aluno: '))
                            if nota < 0 or nota > 10:
                                raise ValueError
                        except ValueError:
                            print('Digite um valor válido!')
                            continue
                        else:
                            lista_das_notas.append(nota)
                    else:
                        dados['notas'] = lista_das_notas
                        dados['media'] = sum(lista_das_notas) / 3
                        if dados['media'] >= 6:
                            situacao_do_aluno = 'aprovado'
                        else:
                            situacao_do_aluno = 'reprovado'
                        dados['situacao'] = situacao_do_aluno
                        print('\nNotas atualizadas!\n')
                elif escolha == '2':
                        novo_nome = input('Digite o novo nome: ').lower().strip()
                        sistema[novo_nome] = sistema.pop(busca)
                        dados = sistema[novo_nome]
                        print('\nNome atualizado!\n')
                elif escolha == '3':
                    while True:
                        novas_informacoes = input('Digite sobre o aluno (MAX 50): ')
                        if len(novas_informacoes) > 50 or len(novas_informacoes) < 3:
                            print('Tente novamente!')
                            continue
                        else:
                            break
                    dados['informacao'] = novas_informacoes
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
        print(f'3. Maior Média: {maior} / Menor Média: {menor}')
        print(f'4. Média da turma: {sum(medias) / len(sistema)}')


# Principal:
opcoes(True, False)
print('Digite o comando "opção" para ver as opções novamente!')
while True:
    print()
    escolha = input('= ').lower()
    print()
    if escolha == 'teste':
        print(sistema)
    elif escolha == 'opção':

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