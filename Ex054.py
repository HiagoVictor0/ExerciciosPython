maior=0
menor=0

for i in  range(0,6):
    ano=int(input('Digite o ano em que nasceu: '))

    if ano <= 2005:
        maior=maior+1
    elif ano >=2006:
        menor=menor+1

print('{} pessoas alcançaram a maioridade'.format(maior))
print('{} pessoas ainda não alcançaram a maioridade'.format(menor))