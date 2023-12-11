class Produto:
    def __init__(self, nome, preco):
        self.nome=nome
        self.preco=preco

    def desconto(self, desconto):
        self.preco=self.preco-(self.preco*(desconto/100))
        
    '''getter'''
    @property
    def preco(self):
        return self._preco
    
    '''setter'''
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor=float(valor.replace('R$', ''))
        self._preco=valor


p1 = Produto('Calça', 300)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preco)