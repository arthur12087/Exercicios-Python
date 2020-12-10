def calcFatorialFor(valorInteiro):
    fatorial = 1

    for i in range(valorInteiro,0,-1):
        fatorial = fatorial *i

    return fatorial

def calcFatorialWhile(valorinteiro):
    cont = valorinteiro
    fatorial = 1
    while cont > 0:
        fatorial = fatorial * cont
        cont = cont - 1
    return fatorial

def main ():
    numInteiro = int(input("Digite seu número inteiro: "))
    print(calcFatorialFor(numInteiro))
    print(calcFatorialWhile(numInteiro))



main()