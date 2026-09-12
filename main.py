# Importações do core/
from core.logica import (
    adicionar_aluno, buscar_aluno, editar_aluno,
    excluir_aluno, gerar_relatorio, listar_alunos
)
from core.armazenamento import (
    salvar_arquivo, carregar_arquivo
)
from core.organizacao import (
    lin, menu
)

# Variáveis principais
menu_principal = {
    "1": "Adicionar Aluno",
    "2": "Listar Alunos",
    "3": "Buscar Aluno",
    "4": "Excluir Aluno",
    "5": "Editar Aluno",
    "6": "Relatório Geral",
    "7": "Sair",
}
menu_edicoes = {
    "1": "Editar Notas",
    "2": "Editar Nome",
    "3": "Editar Informação",
    "4": "Sair"
}

sistema = carregar_arquivo()

# Código Principal
lin("-")
menu(menu_principal)
lin("-")
print('Sempre que quiser ver a tabela digite "menu"!\n')

while True:
    print("Digite o número da opção ou comando que deseja:")
    escolha = input(">> ").lower().strip()

    if escolha == "menu":

        lin("-")
        menu(menu_principal)
        lin("-")

    elif escolha == "1":
        lin("-")
        try:
            # Captura nome do aluno
            print("\nDigite o nome do aluno: ")
            nome_do_aluno = input(">> ")

            # Captura descrição do aluno
            print(f"\nDigite a descrição de {nome_do_aluno.capitalize()}, 3-50 caracteres!")
            informacao_do_aluno = input(">> ")

            # Captura notas do aluno
            notas_do_aluno = []
            while len(notas_do_aluno) != 3:
                try:
                    print(f"\nDigite a nota {len(notas_do_aluno) + 1} de {nome_do_aluno.capitalize()}:")
                    nota_do_aluno = float(input(">> "))

                    notas_do_aluno.append(nota_do_aluno)
                except ValueError:
                    print("\nNota inválida!\n")

            # Salva e registra aluno
            aluno_a_adicionar = adicionar_aluno(nome_do_aluno, notas_do_aluno, informacao_do_aluno)
            sistema.append(aluno_a_adicionar)
            salvar_arquivo(sistema)

            print()
        except ValueError as e:
            print(f"\n{e}\n")

        lin("-")

    elif escolha == "2":

        lin("-")
        try:
            # Lista os alunos
            listar_alunos(sistema)

        except TypeError as e:
            print(f"\n{e}\n")

        lin("-")

    elif escolha == "3":

        lin("-")
        try:
            # Captura nome do aluno
            print("\nDigite o nome do aluno buscado (verifique a opção 2):")
            aluno_buscado = input(">> ")

            # Encontra e imprime o aluno encontrado
            aluno_encontrado = buscar_aluno(sistema, aluno_buscado)
            situacao_do_aluno = "Aprovado" if aluno_encontrado["situacao"] else "Reprovado"

            print(f"\n- {aluno_encontrado['nome'].capitalize()} | Média: {aluno_encontrado['media']:.2f} | {situacao_do_aluno} | {aluno_encontrado['informacao']}\n")

        except TypeError as e:
            print(f"\n{e}\n")

        lin("-")

    elif escolha == "4":

        lin("-")
        try:
            # Captura nome do aluno e encontra aluno
            print("\nDigite o nome do aluno buscado para excluir (verifique a opção 2): ")
            aluno_buscado = input(">> ")
            aluno_encontrado = buscar_aluno(sistema, aluno_buscado)

            # Captura confirmação e valida
            while True:
                print(f"\nRealmente deseja excluir {aluno_encontrado['nome'].capitalize()}? Essa ação é irreversivel! (sim/não):")
                confirmacao = input(">> ").lower().strip()

                if confirmacao in ["sim", "ss", "s"]:
                    excluir_confirmacao = True
                    break

                elif confirmacao in ["não", "nn", "nao", "n"]:
                    excluir_confirmacao = False
                    break

                else:
                    print("\nDigite algo válido!\n")

            # Exclui aluno e salva a exclusão
            aluno_excluido = excluir_aluno(sistema, aluno_encontrado, excluir_confirmacao)
            salvar_arquivo(sistema)

            print(f"Aluno {aluno_excluido['nome'].capitalize()} foi excluído!\n")

        except TypeError as e:
            print(f"\n{e}\n")

        lin("-")

    elif escolha == "5":

        lin("-")
        # Encontra aluno para edições
        try:
            print("\nDigite o nome do aluno buscado:")
            aluno_buscado = input(">> ")

            aluno_para_editar = buscar_aluno(sistema, aluno_buscado)
        except TypeError as e:
            print(f"\n{e}\n")
            continue

        # Entra em edições
        print("\nEntrando em edições...\n")
        try:        
            lin("=")
            menu(menu_edicoes)
            lin("=")
            print('Sempre que quiser ver a tabela de edições digite "edição"!\n')

            while True:
                print("Digite o número da edição ou comando que deseja:")
                escolha_edicao = input(">> ").lower().strip()

                if escolha_edicao in ["edicao", "ediçao", "edição"]: # Visualiza menu

                    lin("=")
                    menu(menu_edicoes)
                    lin("=")
            
                elif escolha_edicao == "1": # Edita notas

                    lin("=")
                    try:
                        # Captura as novas notas do aluno
                        novas_notas = []
                        while len(novas_notas) != 3:
                            try:
                               print(f"\nDigite a nota {len(novas_notas) + 1} do aluno {aluno_para_editar['nome'].capitalize()}:")
                               nova_nota = float(input(">> "))

                               novas_notas.append(nova_nota)

                            except ValueError:
                                print("\nDigite uma nota válida!\n")

                        # Edita as notas, média e situação do aluno:
                        editar_aluno(sistema, aluno_para_editar, novas_notas, "1")
                        salvar_arquivo(sistema)
                        print("\nNotas editadas com sucesso!\n")

                    except ValueError as e:
                        print(f"\n{e}\n")

                    lin("=")

                elif escolha_edicao == "2": # Edita nome

                    lin("=")
                    try:
                        # Captura novo nome
                        print("\nDigite o novo nome:")
                        novo_nome = input(">> ")

                        # Edita, valida e salva novo nome
                        editar_aluno(sistema, aluno_para_editar, novo_nome, "2")
                        salvar_arquivo(sistema)
                        print("\nNome editado com sucesso!\n")

                    except ValueError as e:
                        print(f"\n{e}\n")

                    lin("=")

                elif escolha_edicao == "3":

                    lin("=")
                    try:
                        # Captura nova informacao
                        print("\nDigite a nova informação, 3-50 caracteres!")
                        nova_informacao = input(">> ")

                        # Edita, valida e salva nova informação
                        editar_aluno(sistema, aluno_para_editar, nova_informacao, "3")
                        salvar_arquivo(sistema)
                        print("\nInformação editada com sucesso!\n")

                    except ValueError as e:
                        print(f"\n{e}\n")

                    lin("=")

                elif escolha_edicao == "4":

                    # Captura e válida saida
                    lin("=")
                    while True:
                        print("\nDeseja encerrar edições? (sim/não): ")
                        confirmacao = input(">> ").lower().strip()

                        if confirmacao in ["sim", "ss", "s"]:
                            confirmacao_saida = True
                            break

                        elif confirmacao in ["não", "nao", "nn", "n"]:
                            confirmacao_saida = False
                            break

                        else:
                            print("\nDigite algo válido!\n")

                    if confirmacao_saida:
                        print("\nEncerrando edições, voltando ao menu principal...\n")
                        lin("=")
                        break
                    else:
                        print("\nOperação cancelada.\n")
                        lin("=")
                        continue

                else:
                    print("\nDigite algo válido!\n")

        except TypeError as e:
            print(f"\n{e}\n")

        lin("-")

    elif escolha == "6":
        lin("-")
        try:
            relatorio = gerar_relatorio(sistema)

            lin("=", 40)
            print("     Relatório Geral     ")
            lin("=", 40)

            print(f"\n[1] Quantidades de alunos: {relatorio['quantidade_de_alunos']}")
            print("[2] Aprovados:")
            for aluno in relatorio["aprovados"]:
                print(f"   - {aluno}")

            print("\n[3] Reprovados:")
            for aluno in relatorio["reprovados"]:
                print(f"   - {aluno}")

            print(f"\n[4] Maior média: {relatorio['maior_media']:.2f}")
            print(f"[5] Menor média: {relatorio['menor_media']:.2f}")
            print(f"[6] Média da turma: {relatorio['media_turma']:.2f}\n")

        except TypeError as e:
            print(f"\n{e}\n")

        lin("-")

    elif escolha == "7":
        lin("-")
        confirmacao = None
        while confirmacao not in ["sim", "ss", "s"]:
            print("\nTem certeza que deseja encerrar? (sim/não): ")
            confirmacao = input(">> ").lower().strip()

            if confirmacao in ["não", "nao", "nn", "n"]:
                print("\nOperação Cancelada.\n")
                break

            else:
                print("\nDigite algo válido!\n")

        else:
            print("\nEncerrando...\n")
            break
        lin("-")

    else:
        print("\nDigite algo válido!\n")