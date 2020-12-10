def solução1 (n1,n2):
    calc1 = (n1*2) * (n2/2)
    return calc1

def solução2 (n1,n3):
    calc2 = (n1*3) + (n3)
    return calc2

def solução3 (n3):
    calc3 = n3**3
    return calc3

def main():
    num1 = int(input("digite seu primeiro número:"))
    num2 = int(input("digite seu segundo número:"))
    numReal = float(input("digite seu terceiro número:"))

    resultado1 = solução1(num1,num2)
    resultado2 = solução2(num1,numReal)
    resultado3 = solução3(numReal)
    print(resultado1)
    print(resultado2)
    print(resultado3)

main()

