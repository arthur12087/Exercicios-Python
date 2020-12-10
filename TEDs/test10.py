def main():
    valor = float(input("Digite seu valor para análise: "))
    if valor<0:
        print("Seu valor é negativo")
        
    elif valor>0:
        print("Seu valor é positivo")

    else:
        print("seu valor é um número neutro")
main()