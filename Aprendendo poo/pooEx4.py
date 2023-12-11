class Televisao:
    def __init__(self):
        self.volume=0
        self.canal=1

    def aum_volume(self):
        if self.volume < 100:
            self.volume+=1
            print(f'Volume: {self.volume}')

    def dim_volume(self):
        if  self.volume > 0:
            self.volume -= 1
            print(f'Volume: {self.volume}')

    def trocar_canal(self, canal):
        self.canal = canal

    def aum_canal(self):
        self.canal += 1

    def dim_canal(self):
        self.canal -= 1

    def get_volume(self):
        return self.volume
    
    def get_canal(self):
        return self.canal
    
class ControleRemoto:
    def __init__(self, televisao):
        self.televisao=televisao

    def menu(self):

        while True:
            print('CONTROLE REMOTO')
            print('1 - Aumentar o volume')
            print('2 - Diminuir o volume')
            print('3 - Trocar de canal')
            print('4 - Aumentar o canal')
            print('5 - Diminuir o canal')
            print('6 - Consultar volume e canal')
            print('0 - Parar')

            opcao=int(input('Digite uma opção: '))

            if opcao==1:
                self.televisao.aum_volume()
            
            if opcao==2:
                self.televisao.dim_volume()

            if opcao==3:
                canal=int(input('Digite o canal: '))
                self.televisao.trocar_canal(canal)

            if opcao==4:
                self.televisao.aum_canal()

            if opcao==5:
                self.televisao.dim_canal()

            if opcao==6:
                print('O volume esta em: ', self.televisao.get_volume())
                print('O canal esta em: ', self.televisao.get_canal())

            if opcao==0:
                break

tv = Televisao()
x = ControleRemoto(tv)
x.menu()





