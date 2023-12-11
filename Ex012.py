salario=float(input('Digite o valor do salario: '))

aum=salario*0.15
total=salario+aum

print('Com o desconto de 15% o valor {} fica de {:.2f} reais'.format(salario, total))