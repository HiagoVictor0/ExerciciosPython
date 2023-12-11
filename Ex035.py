a1=int(input('Digite uma reta: '))
a2=int(input('Digite uma reta: '))
a3=int(input('Digite uma reta: '))

if a1+a2<a3 or a2+a3<a1 or a3+a1<a2 :
    print('nao forma um triangulo')

else:
    print('Forma triangulo')