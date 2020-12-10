def main():
    nomeAmigos = []
    datasAniversario = []
    for i in range(0,5):
        nome = str(input("Digite o nome do amigo(a): "))
        data = str(input("digite a data de aniversário dele(a): "))
        nomeAmigos.append(nome)
        datasAniversario.append(data)
    print(nomeAmigos)
    print(datasAniversario)
    removeNome = str(input("deseja remover algum amigo? se sim, informe o nome: "))

    if removeNome in nomeAmigos:
        removeData = str(input("informe a data de aniversário da pessoa: "))
        nomeAmigos.remove(removeNome)
        datasAniversario.remove(removeData)
        print("Amigo removido com sucesso!")
        print(nomeAmigos)
        print(datasAniversario)
    else:
        print("sem remoção!")



main()