def diaDoProgramador (ano):
    anoBissexto = "12.09."
    anoNaoBissexto = "13.09."
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        return anoBissexto+ str(ano)
    else:
        return anoNaoBissexto + str(ano)

def main():
    anoDigitado = int(input("Digite o ano que voce deseja: "))
    print("O dia do programador é ",diaDoProgramador(anoDigitado))

main()