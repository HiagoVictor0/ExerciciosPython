frase=str(input('Digite uma frase: '))
lista=frase.split()
junto=''.join(lista)
inverte=junto[::-1]

if junto==inverte:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')
