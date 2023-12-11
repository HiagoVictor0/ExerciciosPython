dias=int(input('Digite a quantidade de dias que voce usou carro '))
km=float(input('Digite a quantidade de quilometros rodada '))

preco=(60*dias)+(km*0.15)

print('O valor total a se pagar é de {}{}{} reais'.format('\033[7;35;42m', preco, '\033[m'))