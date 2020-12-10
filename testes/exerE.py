def main():
 registros = []
 for i in range(0,5):
     nome = str(input("digite o nome que deseja: "))
     registros.append(nome)
 print(registros)
 nomeAdicional = str(input("digite outro nome: "))
 registros.append(nomeAdicional)

 nomeAdicional2 = str(input("digite o novo nome: "))
 registros.insert(1,nomeAdicional2)
 print(registros)


main()