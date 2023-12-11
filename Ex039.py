ano=int(input('Digite seu ano de nascimento: '))
idade=2023-ano
if idade < 18:
    falta=18 - idade
    print('Ainda faltam {} anos para você ir se alistar'. format(falta))

elif idade==18:
    print('Já está na hora de se alistar meu filho.')

elif idade > 18:
    passou=idade - 18
    print('Ja passou {} anos que você deveria ter se alistado.'.format(passou))