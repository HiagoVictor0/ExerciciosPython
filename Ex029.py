km=float(input('Digite a velocidade em que o carro passou:'))

if km>80: 
    print('O carro foi multado')
    num = km - 80
    multa = num*7.00
    print('Sua multa foi de {:.2f}R$'.format(multa))

else:
    print('Você não foi multado')