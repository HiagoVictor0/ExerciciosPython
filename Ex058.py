from random import randint

count=0
num=randint(1,10)

n=int(input('Digite um numero e tente a sorte: '))

while n!=num:
    print('Numero errado, tente novamente!')
    n=int(input('Digite outro numero: '))
    count+=1
    if n==num:
        print('Você acertou o numero')
        print(f'Você teve {count} respostas erradas')
        break