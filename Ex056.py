somaidade=0
mediaidade=0
maioridade=0
nomevelho=''
count=0

for i in range(1,5):
    print('\033[31m------PESSOA-----\033[m')
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo[M/F]: '))
    somaidade+=idade
    if i==1 and sexo in 'Mm':
        maioridadeh=idade
        nomevelho=nome
    
    if sexo in 'Mm' and idade>maioridade:
        maioridadeh=idade
        nomevelho=nome

    if idade<20 and sexo in 'Ff':
        count=count+1

mediaidade=somaidade/4

print ('A media da idade de todos é de {}' .format(mediaidade))
print('O nome do homem mais velho é {}'.format(nomevelho))
print('{} mulheres tem menos de 20 anos'.format(count))