class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = False

    def exibir_informacoes(self):
        status_venda = "Vendido" if self.vendido else "Disponível"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Status: {status_venda}")
        print("-" * 20)

    def vender(self):
        if not self.vendido:
            self.vendido = True
            print(f"O carro {self.marca} {self.modelo} foi vendido.")
        else:
            print("Este carro já foi vendido.")

    def ajustar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"O preço do carro {self.marca} {self.modelo} foi ajustado para R${novo_preco:.2f}")


# Instanciando pelo menos 5 objetos
carro1 = Carro("Toyota", "Corolla", 2020, 75000.00)
carro2 = Carro("Ford", "Mustang", 2021, 85000.00)
carro3 = Carro("BMW", "X5", 2019, 95000.00)
carro4 = Carro("Honda", "Civic", 2022, 72000.00)
carro5 = Carro("Volkswagen", "Golf", 2020, 68000.00)

# Exibindo informações dos carros
carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
carro4.exibir_informacoes()
carro5.exibir_informacoes()

# Vender um carro
carro1.vender()

# Ajustar o preço de um carro
carro2.ajustar_preco(82000.00)

# Exibir informações atualizadas após as operações
carro1.exibir_informacoes()
carro2.exibir_informacoes()
