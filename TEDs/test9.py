def main():

    produto1 = float(input("qual o preço do primeiro produto?"))
    produto2 = float(input("qual o preço do segundo produto?"))
    produto3 = float(input("qual o preço do terceiro produto?"))

    if produto1<produto2 and produto3:
        print("o produto mais barato é o primeiro")
    elif produto2<produto1 and produto3:
        print("o produto mais barato é o segundo")
    elif produto3< produto1 and produto2:
        print("O produto mais barato é o terceiro")
    elif produto1 or produto2 == produto3:
        print("os produtos mais baratos tem o mesmo valor")
    elif produto3 or produto2 == produto1:
        print("os produtos mais baratos tem o mesmo valor")


main()
