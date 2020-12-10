def main():
    nota1 = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota: "))
    media = (nota1 + nota2) /2

    if media>=7 and media<10:
        print("Parabéns, você foi aprovado")
    elif media == 10:
        print("Parabéns, aprovado com distinção, você é cara!")

    elif media>10:
        print("Insira suas notas corretamente, de 1 a 10")
        main()
    else:
        print("Você está reprovado, te vejo ano que vem")



main()