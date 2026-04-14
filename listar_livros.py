
def listar_livros():
    with open("page.txt", "r", encoding="utf-8") as file:
        livros = file.read()

    print("\n", livros)