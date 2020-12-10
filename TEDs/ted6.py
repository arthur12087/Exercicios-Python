dicionario = {}


def cadastro():
    nome = str(input("informe o nome do cliente: "))
    valor = int(input("informe quanto esse cliente deve: "))
    telefone = str(input("informe o número de telefone: "))
    endereco = str(input("informe o endereço do cliente: "))

    dicionario[nome] = [valor,telefone,endereco]

    desejo = str(input("deseja cadastrar mais algum cliente? (S/N)"))
    if desejo.upper() =="S":
        cadastro()
    else:
        menu() 

def atualizacao():
    buscaCliente = str(input("informe o nome:"))
    if buscaCliente in dicionario.keys():
        novoValor = int(input("digite o novo valor: "))

        dicionario[buscaCliente] =[novoValor]
        print("dívida atualizada!")
        menu()

def removeClientes():
    nomeCliente = str(input("informe o nome do cliente: "))
    if nomeCliente in dicionario.keys():
        dicionario.pop(nomeCliente)
        print("cliente removido!")
        menu()
    else:
        print("erro,tente novamente")
        removeClientes()

def buscaNome():
    nomeBusca = str(input("informe o nome para busca:"))
    if nomeBusca in dicionario.keys():
        print(dicionario[nomeBusca])
        menu()

def menu():
    print("DIGITE 1 PARA CADASTRAR\n"
          "DIGITE 2 PARA ATUALIZAR UM VALOR\n"
          "DIGITE 3 PARA REMOVER ALGUM CLIENTE\n"
          "DIGITE 4 PARA BUSCAR NOME DE UM CLIENTE\n")
    num = str(input(":"))

    if num == "1":
        cadastro()
    if num == "2":
        atualizacao()
    if num == "3":
        removeClientes()
    if num =="4":
        buscaNome()

menu()