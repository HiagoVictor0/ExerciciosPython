peso=float(input('Digite o seu peso: '))
altura=float(input('Digite sua altura: '))

imc=peso/(altura*altura)

if imc<=18.4:
    print('\033[31mAbaixo do peso\033[m')

elif imc>=18.5 and imc<=25:
    print('\033[32mPeso ideal\033[m')

elif imc>=25 and imc<=30:
    print('\033[33mSobrepeso\033[m')

elif imc>=30 and imc<=40:
    print('\033[31mObesidade\033[m')

else:
    print('\033[31mObesidade morbida\033[m')