def main():
    dicionario = {}
    for i in range(5):
        nomeUsuario = str(input("informe Seu nome:"))
        dataNascimento =  str(input("informe sua data de nascimento:"))
        endereco = str(input("informe Seu endereço:"))

        dicionario[nomeUsuario] = [dataNascimento,endereco]

    print(dicionario)

main()