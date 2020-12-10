def main():
 nomeDePaises = []
 for i in range(0,5):
     nomepais = str(input("digite o nome do país que deseja: "))
     nomeDePaises.append(nomepais)
 print(nomeDePaises)

 nomeDeCidades = list()
 cont = 0
 while cont<5:
     nomeCidade = str(input("digite o nome da cidade que deseja: "))
     nomeDeCidades.append(nomeCidade)
     cont= cont +1
 print(nomeDeCidades)

main()