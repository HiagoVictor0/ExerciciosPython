class Pessoa:

    ano_atual = 2023

    def __init__(self, nome, data_nascimento, altura):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__altura = altura
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def get_data_nascimento(self):
        return self.__data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
        
    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura):
        self.__altura = altura
        
    def imprimir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Data de nascimento: {self.__data_nascimento}")
        print(f"Altura: {self.__altura}m")

    def calcular_idade(self):
        return print(self.ano_atual - self.__data_nascimento)

p1 = Pessoa('Marcos', 2002, 1.83)

p1.imprimir_dados()
p1.calcular_idade()

