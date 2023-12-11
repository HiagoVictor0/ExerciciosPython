import random

P1=str(input('Digite o nome de uma pessoa: '))
P2=str(input('Digite o nome de uma pessoa: '))
P3=str(input('Digite o nome de uma pessoa: '))
P4=str(input('Digite o nome de uma pessoa: '))

lista=[P1, P2, P3, P4]

random.shuffle(lista)

print('A ordem dos alunos é: ')
print(lista)