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
            listar_alunos(sistema)

        except TypeError as e:
            print(f"\n{e}\n")

        lin("-")

    elif escolha == "3":
        pass

    elif escolha == "4":
        pass

    elif escolha == "5":
        pass

    elif escolha == "6":
        pass

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