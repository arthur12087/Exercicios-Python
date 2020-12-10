def main():

    letraDigitada = input("Digite sua letra para análise, F ou M para Feminino ou Masculino: ")
    if letraDigitada.upper() == "F":
        print("O gênero é Feminino - ", letraDigitada)

    elif letraDigitada.upper() == "M":
        print("O gênero é Masculino - ",letraDigitada)
    else:
        print("Gênero inválido")
        main()

main()


