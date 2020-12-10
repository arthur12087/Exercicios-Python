def main():
    nomeDasCores = []
    for i in range(0,5):
        nomeCor = str(input('digite o nome da cor que deseja: '))
        nomeDasCores.append(nomeCor)

    if "vermelho" in nomeDasCores:
        nomeDasCores.remove("vermelho")
    print(nomeDasCores)
    
main()