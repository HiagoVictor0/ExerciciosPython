nota1=float(input('Digite a sua nota: '))
nota2=float(input('Digite a sua segunda nota: '))

media=  (nota1+nota2)/2

if media < 5.0:
    print('\033[31mReprovado\033[m')

elif media >= 5.0 and media < 7.0:
    print('\033[33mRecuperação\033[m')

elif media >= 7:
    print('\033[32mAprovado\033[m')