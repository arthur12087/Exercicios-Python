def main():
    dicionario = {}

    dicionario['codigo de barra 1'] = ['laranja',5]
    dicionario['codigo de barra 2'] = ['uva',3]
    dicionario['codigo de barra 3'] = ['maça',2]
    dicionario['codigo de barra 4'] = ['leite', 7]
    dicionario['codigo de barra 5'] = ['kiwi', 4]
    dicionario['codigo de barra 6'] = ['melão', 9]

    dicionario.pop('codigo de barra 3')
    dicionario.pop('codigo de barra 4')

    del (dicionario['codigo de barra 1'])
    del (dicionario['codigo de barra 2'])

    print(dicionario)
main()