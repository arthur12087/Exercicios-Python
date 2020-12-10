def main():
    matriz = [[], [], []]

    for i in range(3):
        nome = str(input("Digite seu nome: "))
        matriz[0].append(nome)

        matricula = str(input("Digite sua matricula"))
        matriz[1].append(matricula)

        dataNascimento = str(input("informe sua data de nascimento no formato D/M/A:"))
        matriz[2].append(dataNascimento)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print("%8s" % matriz[i][j], end='')
        print()

main()