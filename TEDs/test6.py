tamanho = float(input("Digite o a área total em metros quadrados:"))
totalLitros = tamanho/3

totalLatas = totalLitros/18
custoTotal = totalLatas*80

if totalLatas != int:
    totalLatas = round(totalLatas +0.5)

print("O total de latas necessárias são",totalLatas,"e o custo total será de", round(custoTotal,2),"reais")
