def main():
    matriz = [[1,2,3,4],[5,6,7,8]]
    valor = int(input("insira o valor: "))
    matriz[0].append(valor)
    matriz[1].append(valor)
    print(matriz)


main()