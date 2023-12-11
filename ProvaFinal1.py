import math
'''classe Ponto que representa um ponto no plano cartesiano'''
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    '''método distancia_ate que calcula a distância entre dois pontos.'''
    def distancia_ate(self, outro):
        distancia = math.sqrt((self.x - outro.x)**2 + (self.y - outro.y)**2)
        return distancia
    '''método ponto_mais_proximo na classe Ponto que recebe uma lista de pontos e retorna o ponto mais próximo ao objeto atual.'''
    '''O método funciona percorrendo a lista de pontos e calculando a distância entre cada um deles e o objeto atual usando 
    o método distancia_ate. O ponto com menor distância é armazenado em uma variável mais_proximo e sua distância é armazenada 
    em uma variável distancia_minima.'''
    def ponto_mais_proximo(self, pontos):
        distancia_minima = float('inf')
        mais_proximo = None
        for p in pontos:
            if p is not self:
                d = self.distancia_ate(p)
                if d < distancia_minima:
                    distancia_minima = d
                    mais_proximo = p
        return mais_proximo
    
pontos = []
for i in range(5):
    x, y = map(float, input(f"Digite as coordenadas do ponto {i+1}: ").split())
    p = Ponto(x, y)
    pontos.append(p)

primeiro_ponto = pontos[0]
ponto_mais_proximo = primeiro_ponto.ponto_mais_proximo(pontos)
distancia = primeiro_ponto.distancia_ate(ponto_mais_proximo)

print(f"A distância entre o primeiro ponto ({primeiro_ponto.x}, {primeiro_ponto.y}) e o mais próximo ({ponto_mais_proximo.x}, {ponto_mais_proximo.y}) é {distancia}.")