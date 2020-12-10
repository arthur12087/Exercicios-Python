def main():
    totalElementos = int(input("digite quantos elementos voce deseja que sua array tenha: "))
    registro = []
    for i in range(0,totalElementos):
        valores = int(input('digite seu valor de elemento '+ str(i+1) +': '))
        registro.append(valores)
    print(registro)


main()