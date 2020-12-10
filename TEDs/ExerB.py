def main():
    matriz = [[39*7,14*7,27*7],[21*7,83*7,92*7],[31*7,12*7,43*7]]


    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print("%4d" % matriz[i][j], end='')
        print()



main()