salario=float(input('Digite o seu salario: '))

if salario > 1250.00:
    aum=salario+(salario*0.10)
else:
    aum=salario+(salario*0.15)

print('Seu salario agora é: {:.2f}'.format(aum))