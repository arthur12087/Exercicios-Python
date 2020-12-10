def main():
    numero = str(input("Digite o número para análise: "))
    numeroInverso = numero[::-1]

    if numero == numeroInverso:
        print("seu número É um palíndromo")
    else:
        print("Ih rapaz, seu número NÃO é um palíndromo...")
        

main()