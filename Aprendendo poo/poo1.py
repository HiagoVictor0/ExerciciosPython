from random import randint

class Pessoa:

    ano_atual = int(2023)

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome=nome
        self.idade=idade
        self.comendo=comendo
        self.falando=falando

    def parar_comer(self):
        if not self.comendo:
            print('{} não está comendo'.format(self.nome))
            return
        print('{} parou de comer.'.format(self.nome))
        self.comendo = False
        
    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} nao pode falar enquanto come')
            return
        
        if self.comendo:
            print('{} ja está comendo.'.format(self.nome))
            return
        print('{} esta comendo {}'.format(self.nome, alimento))
        self.comendo = True

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} Nao pode falar comendo')
            return

        if self.falando:
            print('{} ja está falando.'.format(self.nome))
            return
        
        print('{} está falando sobre {}'.format(self.nome, assunto))
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        print(f'{self.nome} parou de falar.')
    
    def ano_nascimento(self):
        return print(self.ano_atual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade=cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gerar_id():
        rand=randint(10000, 19999)
        return rand
    
p1=Pessoa('Hiago', 18)
p2=Pessoa('Marcos', 23)
p3=Pessoa('Anna', 18)

p1.ano_nascimento()
p1=Pessoa.por_ano_nascimento('Hiago', 2004)

print(p1.gerar_id())
