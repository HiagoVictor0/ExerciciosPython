class BancoDeDados:
    def __init__(self):
        self.dados={}

    def inserir_clientes(self, id, nome):
        if 'Clientes' not in self.dados:
            self.dados['Clientes']={id: nome}

        else:
            self.dados['Clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['Clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['Clientes'][id]


bd=BancoDeDados()

bd.inserir_clientes(1, 'Anna')
bd.inserir_clientes(2, 'Hiago')
bd.inserir_clientes(3, 'Lazim')

bd.apaga_cliente(2)
bd.lista_clientes()