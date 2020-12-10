def main():
 listaNomes = ["Arthur"]
 for i in range(0,5):
     nomeDigitado = str(input("digite o nome: "))
     listaNomes.append(nomeDigitado)
 print(listaNomes)

 listaNomes.remove("Arthur")
 listaNomes.insert(0,"Harrysson")
 print(listaNomes)


main()