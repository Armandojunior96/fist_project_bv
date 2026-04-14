class Carro:
    def __init__(self, nome_do_carro, cor_do_carro, ano_de_fabrico):
        self.cor_do_carro = cor_do_carro
        self.nome_do_carro = nome_do_carro
        self.ano_de_fabrico = ano_de_fabrico


carro1 = Carro("Toyota", "Branco", "2002")
carro2 = Carro("Fiat", " Preto","2023")
carro3 = Carro("Corola", "Marrom", "2009")


print(f"Carro1: {carro1.nome_do_carro} | Cor: {carro1.cor_do_carro} | Ano de fabricação: {carro1.ano_de_fabrico}")
print(carro2.nome_do_carro)
print(carro3.nome_do_carro)