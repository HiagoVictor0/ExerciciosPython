class Elevador:
    def __init__(self):
        self.andar_atual=0
        self.total_andares=0
        self.capacidade=0
        self.pessoas_presentes=0

    def iniciar(self, capacidade, total_andares):
        self.capacidade=capacidade
        self.total_andares=total_andares
        self.pessoas_presentes=0
        self.andar_atual=0

    def entra(self):
        if self.pessoas_presentes < self.capacidade:
            self.pessoas_presentes += 1
            print('\033[32m\nUma pessoa entrou no elevador.\033[m\n')
        else:
            print('\033[31m\nO elevador esta lotado.\033[m\n')

    def sai(self):
        if self.pessoas_presentes > 0:
            self.pessoas_presentes -= 1
            print('\033[032mUma pessoa saiu do elevador.\033[m\n')
        else:
            print('\033[031mO elevador está vazio.\033[m\n')

    def sobe(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            print('\033[032mO elevador está no andar ', self.andar_atual, '\033[m')

        else:
            print('\033[031mVocê chegou no último andar.\033[m\n')

    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print('\033[032mVocê desceu para o andar ', self.andar_atual, '\033[m')

        else:
            print('\033[032mVocê chegou no térreo.\033[m\n')

    def get_andar_atual(self):
        return self.andar_atual
    
    def get_total_andares(self):
        return self.total_andares
    
    def get_capacidade(self):
        return self.capacidade
    
    def get_pessoas_presentes(self):
        return self.pessoas_presentes
    
elevador=Elevador()
#Menu iterativo

while True:
    print('Menu elevador\n')
    print('Digite 1: para inicializar.')
    print('Digite 2: para uma pessoa entrar.')
    print('Digite 3: para uma pessoa sair.')
    print('Digite 4: para subir um andar.')
    print('Digite 5: para descer um andar.')
    print('Digite 6: para status.')
    print('Digite 0: para sair.')

    opcao=int(input('\n'))

    if opcao==1:
        capacidade=int(input('Digite a capacidade do elevador: '))
        total_andares=int(input('Digite o total de andares no prédio: '))
        elevador.iniciar(capacidade, total_andares)
        print('Elevador está em funcionamento.')

    if opcao==2:
        elevador.entra()

    if opcao==3:
        elevador.sai()

    if opcao==4:
        elevador.sobe()

    if opcao==5:
        elevador.desce()

    if opcao==6:
        print('Andar atual: ', elevador.get_andar_atual())
        print('Total de andares(excluindo o térreo): ', elevador.get_total_andares())
        print('Capacidade do elevador: ', elevador.get_capacidade())
        print('Pessoas presentes: ', elevador.get_pessoas_presentes())

    if opcao==0:
        break