import random

A1=str(input('Digite o nome do primeiro aluno: '))
A2=str(input('Digite o nome do segundo aluno: '))
A3=str(input('Digite o nome do terceiro aluno: '))
A4=str(input('Digite o nome do quarto aluno: '))

lista = [A1, A2, A3, A4]
escolhido=random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))