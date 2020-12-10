def main():
    listaAnos = []
    for i in range(0,5):
        ano = int(input("digite o ano de nascimento da pessoa: "))
        listaAnos.append(ano)
    listaAnos.sort()
    print(listaAnos)
    listaAnos.sort(reverse=True)
    print(listaAnos)


main()