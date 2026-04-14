from cadastrar_livros import cadastrar_livros
from listar_livros import listar_livros

while True:

    print("\nMenu Principal\n")
    print("1 - Cadastrar Livros")
    print("2 - Listar livros")
    print("3 - Buscar Livros")
    print("4 - Emprestar Livros")
    print("5 - Devolver Livros")
    print("6 - Remover Livros")
    print("0 - Sair\n")

    Op = int(input("Digite a opcao: "))

    if Op==1:
        titulo_livro = input("Digite o titulo: ")
        id_livro = int(input("Digite o ID do livro: "))

        cadastrar_livros(titulo_livro, id_livro)
    elif Op==2:
        listar_livros()
    elif Op==3:
        print("\nLivros Buscados")
    elif Op==4:
         print("\nLivros Emprestastados")
    elif Op==5:
        print("\nLivros Devolvidos")
    elif Op==6:
        print("\nLivros  Removidos")
    elif Op==0:
        print("Log off")
        break
    else:
        print("Opcao Invalida")


