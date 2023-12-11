a1=int(input('Digite uma reta: '))
a2=int(input('Digite uma reta: '))
a3=int(input('Digite uma reta: '))

if a1+a2<a3 or a2+a3<a1 or a3+a1<a2 :
    print('nao forma um triangulo')

else:
    print('Forma triangulo')
    
    if a1==a2 and a2==a3:
        print('EQUILATERO')

    elif a1==a2 or a2==a3 or a1==a3:
        print('ISOCELIS')

    else:
        print('ESCALENO')