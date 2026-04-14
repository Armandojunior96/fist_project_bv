def cadastrar_livros(titulo, id_livro):
    with open("page.txt", "a", encoding="utf-8") as file:
        file.write(f"Titulo: {titulo} | ID: {id_livro}\n")

    print("Livro cadastrado com sucesso!")