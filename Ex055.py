pesos=[]

for i in range (0,5):
    peso=float(input('Digite seu peso: '))
    pesos.append(peso)

pesos.sort()

print('O maior peso é: {}'.format(pesos[-1]))
print('O menor peso é: {}'.format(pesos[0]))


