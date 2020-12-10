def main():
    dicionario = {}
    for i in range(2):
        cep = int(input("informe seu CEP:"))
        endereco = str(input("informe o endereco do seu cep:")) 
        dicionario[cep] = [endereco]

    for j in dicionario.keys():
        print("CEP:",j)

main()