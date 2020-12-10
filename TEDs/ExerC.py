def main():
    matriz = [[39,14,27],[21,83,92],[31,12,43]]

    for i in range(len(matriz)):
        if 27 in matriz[i]:
            matriz[i].remove(27)
        if 92 in matriz[i]:
            matriz[i].remove(92)
        if 43 in matriz[i]:
            matriz[i].remove(43)
        for j in range(len(matriz[i])):
            print("%4d" % matriz[i][j], end='')
        print()


main()