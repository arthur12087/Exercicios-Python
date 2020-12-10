def numVelasAniversario (velasAltura):
    qtdAlturasmaximas = velasAltura.count(max(velasAltura))
    return qtdAlturasmaximas

def main():
    totalVelas = int(input("digite o total de velas:"))
    alturaVelas = []
    if totalVelas>10**5 or totalVelas<1:
        print("Inválido, tente novamente")
        return main()

    for i in range(0,totalVelas):
        valoresAlturaVelas = int(input("informe a altura da vela "+ str(i+1) + ": "))
        alturaVelas.append(valoresAlturaVelas)
        if valoresAlturaVelas>10**7 or valoresAlturaVelas<1:
            print("Número inválido, tente de novo")
            return main()

    print("Número de velas com altura máxima é ",numVelasAniversario(alturaVelas))

main()