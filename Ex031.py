km=float(input('Digite a distancia da viagem que você quer fazer: '))

if km > 200:
    preco=km*0.45
else:
    preco=km*0.50

print('Você irá pagar um total de {:.2f} R$'.format(preco))