n1=int(input('Digite um numero: '))
n2=int(input('Digite um numero: '))
n3=int(input('Digite um numero: '))

if n1 > n2 and n1 > n3:
    print('{} é o maior numero'.format(n1))
elif n2 > n1 and n2 > n3:
     print('{} é o maior numero'.format(n2))
else:
     print('{} é o maior numero'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor numero'.format(n1))
elif n2 < n1 and n2 < n3:
     print('{} é o menor numero'.format(n2))
else:
     print('{} é o menor numero'.format(n3))