def main():
    matriz = []
    for i in range(0,4):

        valor1 = int(input("digite um valor: "))
        valor2 = int(input("digite um valor: "))
        valor3 = int(input("digite um valor: "))
        valor4 = int(input("digite um valor: "))
        matriz.append([valor1,valor2,valor3,valor4])

    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (matriz[i][j]>10):
                contador +=1

    print(contador,"valores são maiores que 10")
main()