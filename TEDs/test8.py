def calcImpostoSindicato (salarioBruto):

    valorImpostoSindicato = salarioBruto*0.05
    return valorImpostoSindicato

def calcImpostoINSS (salarioBruto):

    valorImpostoINSS = salarioBruto*0.08
    return valorImpostoINSS


def calcImpostoRenda (salarioBruto):

    valorImpostoRenda = salarioBruto*0.11
    return valorImpostoRenda

def calcSalarioBruto (salarioHora,horasMes):

    salarioTotal = salarioHora*horasMes
    return salarioTotal

def main ():
    salaHora = float(input("Quanto você ganha por hora?"))
    horasMes = float(input("quantas horas você trabalha no mês?"))

    salarioBruto = calcSalarioBruto(salaHora,horasMes)
    impostoRenda = calcImpostoRenda(calcSalarioBruto(salaHora,horasMes))
    impostoINSS = calcImpostoINSS(calcSalarioBruto(salaHora, horasMes))
    impostoSindicato = calcImpostoSindicato(calcSalarioBruto(salaHora, horasMes))

    valorDescontado = impostoINSS + impostoRenda +impostoSindicato
    salarioLiquido = salarioBruto - valorDescontado

    print("Seu salário bruto é de",salarioBruto)
    print("Você pagou",impostoRenda,"de imposto de renda")
    print("Você pagou", impostoINSS, "de imposto de INSS")
    print("Você pagou", impostoSindicato, "de imposto de sindicato")
    print("Seu salário líquido é de",salarioLiquido)
    print("O valor descontado de seus impostos é",valorDescontado)



main()