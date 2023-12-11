preco=float(input('Digite o valor do produto: '))

desc=preco*0.05
valor=preco-desc

print('Com o desconto de 5% o valor {} fica de {:.2f} reais'.format(preco, valor))