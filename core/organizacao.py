# Módulo para a organização e exibição dos menus em main.py

def lin(char, qtd=30):
    print(char * qtd)

def menu(obj):
    if isinstance(obj, dict):
        for nu, opcao in obj.items():
            print(f"{nu}. {opcao}")
    else:
        print(f"\nO objeto precisa ser um dict!\n")