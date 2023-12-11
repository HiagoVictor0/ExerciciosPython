import random
lista=['pedra', 'papel', 'tesoura']
pc=random.choice(lista)
x=str(input('Escolha entre pedra, papel ou tesoura: '))
print('O pc escolheu {}'.format(pc))

if x=='papel' and pc=='papel' or x=='pedra' and pc=='pedra' or x=='tesoura' and pc=='tesoura':
    print('EMPATE')

elif x=='papel' and pc=='pedra' or x=='tesoura' and pc=='papel' or x=='pedra' and pc=='tesoura':
    print('VOCÊ GANHOU!!!')

elif pc=='papel' and x=='pedra' or pc=='tesoura' and x=='papel' or pc=='pedra' and x=='tesoura':
    print('O PC GANHOU OTÁRIO.')

else:
    print('Ninguem ganhou por que voce é burro')