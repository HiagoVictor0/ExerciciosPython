preco=float(input('Digite o valor do produto: '))
print('\n\033[1;41mQual será a forma de pagamento:\033[m\n-Digite 1 para a vista(dinheiro).\n-Digite 2 para a vista(cartão)\n-Digite 3 para parcelar no cartão')
num=int(input())

if num==1:
    valor=preco-(preco*0.1)
    print('O valor a vista é {:.2f}'.format(valor))

elif num==2:
    valor=preco-(preco*0.05)
    print('O valor a vista no cartão é {:.2f}'.format(valor))

elif num==3:
    parcela=int(input('Em quantas vezes você vai parcelar?'))

    if parcela<3:
        print('O valor continua o mesmo {:.2f}'.format(preco))

    elif parcela>2:
        valor=preco+(preco*0.2)
        vm=valor/parcela
        print('O valor total ficará {:.2f} e o valor mensal {:.2f}'.format(valor, vm))

else:
    print('Ta vendo a tabela nao otario, so os numeros d tabela encima')

