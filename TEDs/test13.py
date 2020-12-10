def main():
    numClientes = int(input("digite o total de clientes anteriores:"))

    tempoTotal = 0
    for i in range(0,numClientes):

        tempoClientes = float(input("digite o tempo de espera do cliente:"))
        tempoTotal = tempoTotal + tempoClientes

    media = tempoTotal/numClientes
    print("Tempo de espera médio:",media)






main()