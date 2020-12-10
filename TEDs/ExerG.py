def main():
    matriz = [[2,3,5],[-1,-2,1]]
    matrizTransposta = []

    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            print("%4d"% matriz[j][i],end='')
        print()

main()