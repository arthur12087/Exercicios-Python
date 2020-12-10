def main():
    dicionario = {}
    for i in range(2):
        cep = str(input("informe seu CEP:"))
        endereco = str(input("informe o endereco do seu cep:"))
        dicionario[cep] = [endereco]

    busca = input("informe o conteudo que deseja buscar:")
    for i,j in dicionario.items():
        if busca in dicionario.keys():
            print("o CEP:",busca, "está presente")
            break
        elif busca in j[0]:
            print("o endereço:",busca,"está presente")
            break
        else:
            print("essa informação não existe")


main()