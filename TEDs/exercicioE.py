def main():
    dicionario = {}
    for i in range(3):
        usuario = str(input("informe o nome do usuario: "))
        nome = str(input("informe o nome: "))
        endereco = str(input("informe o endereço:"))
        cpf = str(input("informe o CPF: "))


        dicionario[usuario] = [nome,endereco,cpf]

    for i,j in dicionario.items():
        print(i,j)

main()