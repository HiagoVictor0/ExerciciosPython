import random 
num=random.randint(1,5)

num1=int(input('Digite um numero de 1 a 5: '))

if num1 == num:
    print('Você acertou o numero.')
else:
    print('Você errou o numero.')