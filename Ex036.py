valor=float(input('Qual o valor da casa: '))
salario=float(input('De quanto é o salario do comprador: '))
anos=int(input('E em quantos anos ele vai pagar: '))
meses=anos*12
prestacao=valor/meses
limite=salario*0.3

if prestacao>limite:
    print('\033[;;31mSeu empréstimo foi negado\033[m')
else:
    print('\033[;;32mSeu emprestimo foi concedido\033[m')