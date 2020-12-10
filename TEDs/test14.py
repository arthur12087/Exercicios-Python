def main():
    inicioSeq = int(input("digite o número de início da sequencia: "))
    fimSeq = int(input("digite o numero final da sequencia"))



    for i in range(inicioSeq,fimSeq+1):
        numSequencial = inicioSeq**2
        print(numSequencial)
        inicioSeq += 1



main()