ano=int(input('Digite o ano em que voce nasceu: '))
idade = 2023 - ano

if idade<8:
    print('MIRIM')
elif idade>8 and idade < 15:
    print('INFANTIL')
elif idade>14 and idade < 20:
    print('JUNIOR')
elif idade==20:
    print('SENIOR')
else:
    print('MASTER')