class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome=nome
        self.idade=idade
        self.altura=altura 

class Agenda:
    def __init__(self):
        self.pessoas=[]

    def armazenar_pessoa(self, pessoa):
        if len(self.pessoas) >= 10:
            print('A agenda está cheia.')

        else:
            self.pessoas.append(pessoa)
            print(f'{pessoa.nome} foi adicionade na agenda')

    def remove_pessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome==nome:
                self.pessoas.remove(pessoa)
                print(f'A {pessoa.nome} foi removida')
                return
        print('A pessoa não foi enconstrada.')
        

    def busca_pessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome==nome:
                print('Pessoa encontrada:')
                print(f'nome: {pessoa.nome}')
                print(f'Idade: {pessoa.idade}')
                print(f'Altura: {pessoa.altura}')
                return
            
        print('Pessoa não encontrada.')

    def imprimir_agenda(self):
        for pessoa in self.pessoas:
            print(f'nome: {pessoa.nome}')
            print(f'Idade: {pessoa.idade}')
            print(f'Altura: {pessoa.altura}\n')
            
            
agenda=Agenda()
p1=Pessoa('Kenny', 20, 1.78)
agenda.armazenar_pessoa(p1)
p2=Pessoa('Marcos', 20, 1.86)
agenda.armazenar_pessoa(p2)
p3=Pessoa('Hiago', 18, 1.85)
agenda.armazenar_pessoa(p3)
agenda.imprimir_agenda()

agenda.busca_pessoa('Hiago')
agenda.remove_pessoa('Marcos')
agenda.busca_pessoa('Marcos')

