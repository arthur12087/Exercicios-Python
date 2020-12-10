def main():
    numeroRecebido = int(input("Digite seu número para exibir sua tabuada: "))
    cont= 0

    for i in range(1,11):
        cont = cont + 1
        calctabuada = numeroRecebido * cont
        print(numeroRecebido, "X", cont, "=",calctabuada)



main()