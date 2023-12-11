class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

'''Aqui definimos a classe Produto que possui três atributos: id, nome e preco.'''

class Funcionario:
    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo

'''Aqui definimos a classe Funcionario que possui três atributos: id, nome e cargo.'''

class Pedido:
    def __init__(self, id, funcionario):
        self.id = id
        self.produtos = []
        self.funcionario = funcionario
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total
    
'''Aqui definimos a classe Pedido que possui três atributos: id, produtos e funcionario. 
Ela também possui dois métodos: adicionar_produto, que adiciona um produto na lista de produtos do pedido, 
e calcular_total, que calcula o preço total do pedido com base nos preços dos produtos adicionados.'''
    
class Lanchonete:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

'''Aqui definimos a classe Lanchonete que possui três atributos: nome, endereco e telefone. 
Ela também possui um método adicionar_funcionario, que adiciona um funcionário na lista de funcionários da lanchonete.'''

class InterfaceLanchonete:
    def __init__(self):
        self.lanchonete = Lanchonete("Minha Lanchonete", "Rua A, 123", "(99) 9999-9999")
        self.produtos = {}
        self.funcionarios = {}
        self.pedidos = {}
        self.proximo_id_pedido = 1
        
    def adicionar_produto(self, id, nome, preco):
        produto = Produto(id, nome, preco)
        self.produtos[id] = produto
    
    def adicionar_funcionario(self, id, nome, cargo):
        funcionario = Funcionario(id, nome, cargo)
        self.funcionarios[id] = funcionario
        self.lanchonete.adicionar_funcionario(funcionario)
    
    def criar_pedido(self, funcionario_id):
        if funcionario_id not in self.funcionarios:
            raise Exception("Funcionário não encontrado.")
        funcionario = self.funcionarios[funcionario_id]
        pedido = Pedido(self.proximo_id_pedido, funcionario)
        self.pedidos[self.proximo_id_pedido] = pedido
        self.proximo_id_pedido += 1
        return pedido.id
    
    def adicionar_produto_a_pedido(self, pedido_id, produto_id):
        if pedido_id not in self.pedidos:
            raise Exception("Pedido não encontrado.")
        if produto_id not in self.produtos:
            raise Exception("Produto não encontrado.")
        produto = self.produtos[produto_id]
        pedido = self.pedidos[pedido_id]
        pedido.adicionar_produto(produto)

'''Aqui definimos a classe InterfaceLanchonete que possui quatro atributos: lanchonete, produtos, funcionarios, pedidos e proximo_id'''



'''Para mostrar como esse código funciona, podemos criar uma instância da classe InterfaceLanchonete e realizar algumas operações:'''


# Criando a instância da classe InterfaceLanchonete
interface = InterfaceLanchonete()

# Adicionando alguns produtos
interface.adicionar_produto(1, "Café", 2.50)
interface.adicionar_produto(2, "Pão de queijo", 3.00)
interface.adicionar_produto(3, "Sanduíche", 8.50)

# Adicionando alguns funcionários
interface.adicionar_funcionario(1, "João", "atendente")
interface.adicionar_funcionario(2, "Maria", "cozinheiro")

# Criando um pedido para o funcionário com id 1
pedido_id = interface.criar_pedido(1)


# Adicionando produtos ao pedido
interface.adicionar_produto_a_pedido(pedido_id, 1)
interface.adicionar_produto_a_pedido(pedido_id, 2)
interface.adicionar_produto_a_pedido(pedido_id, 3)

# Calculando o total do pedido
pedido = interface.pedidos[pedido_id]
total = pedido.calcular_total()

# Imprimindo o total
print(f"Total do pedido {pedido_id}: R${total:.2f}")



'''Esse código deve imprimir
Total do pedido 1: R$14.00. Isso significa que o pedido foi criado para o funcionário João, 
e foram adicionados três produtos a ele (Café, Pão de queijo e Sanduíche), totalizando R$ 14,00.'''
