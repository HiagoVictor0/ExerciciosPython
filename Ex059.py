n1=float(input('Digite um numero: '))
n2=float(input('Digite outro valor: '))

num = 0

while num != 5:

    print('\n1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Novos numeros')
    print('5 - Sair do programa\n')
    num=int(input())

    if num == 1:
        valor=n1+n2
        print(f'A soma dos valores {n1} e {n2} é igual a {valor}\n')

    elif num == 2:
        valor=n1*n2
        print(f'A multiplicação dos valores {n1} e {n2} é igual a {valor}\n')

    elif num == 3:
        if n1 > n2:
            maior=n1
            print(f'O valor maior é {maior}\n')

        elif n1==n2:
            print('Os valores são iguais.\n')

        else:
            maior=n2
            print(f'O valor maior é {maior}\n')

    elif num == 4:
        n1=float(input('Digite novos numeros: '))
        n2=float(input('Digite novos numeros: '))

    elif num == 5:
        break

    else:
        print('Digite um dos numeros das opções')