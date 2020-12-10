class Fila():
    def __init__(self):
        self.placaCarros = []

    def inserirPlacaCarro(self, novoDado):
        self.placaCarros.append(novoDado)

    def removerPlacaCarro(self, placaDoCarro):
        for i in self.placaCarros:
            self.placaCarros.pop(0)
            if i == placaDoCarro:
                break

    def getPlacaCarros(self):
        return self.placaCarros

varFila = Fila()

def menu():
    print("=== ESTACIONAMENTO DO MANOEL ===\n"
          "DIGITE 1 PARA CADASTRAR UM NOVO CARRO\n"
          "DIGITE 2 PARA REMOVER UM DETERMINADO CARRO\n"
          "DIGITE S PARA VER ESTADO DO ESTACIONAMENTO\n")

    escolha = str(input(""))

    if escolha == "1":
        placaCarro = str(input("informe a placa do carro para cadastro: "))
        varFila.inserirPlacaCarro(placaCarro)
        print("carro cadastrado\n")
        menu()

    elif escolha == "2":
        placaCarro = str(input("informe a placa do carro para remoção: "))
        varFila.removerPlacaCarro(placaCarro)
        print("carro removido!\n")
        menu()

    elif escolha.upper() == "S":
        print(varFila.getPlacaCarros())
        print("\n")
        menu()

    else:
        print("Não existe essa função!")
        menu()

menu()