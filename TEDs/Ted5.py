matriz = [[0,0,0],[0,0,0],[0,0,0]]
def alterarAtt():
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                matriz[i][j] = "_"

            if matriz[i][j] == 1:
                matriz[i][j] = "X"

            if matriz[i][j] == -1:
                matriz[i][j] = "O"




matriz = [[0,0,0],[0,0,0],[0,0,0]]
def main():
    print("informe 1 para X, e -1 para O")
 
    for i in range(3):

        for j in range(3):
            print("Vez de X\n")
            linha = int(input("informe o número da linha:"))
            coluna = int(input("informe o número da coluna:"))
            matriz[linha-1][coluna-1] = 1

            print("Vez de O\n")
            linha = int(input("informe o número da linha:"))
            coluna = int(input("informe o número da coluna:"))
            matriz[linha-1][coluna-1] = -1

        alterarAtt()
        print(matriz)


main()


