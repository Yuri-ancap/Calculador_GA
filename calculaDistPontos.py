import math

class Ponto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def X(self):
        return self._x

    @property
    def Y(self):
        return self._y

def calcular_distancia(ponto_1, ponto_2):
    return math.sqrt((ponto2.X - ponto1.X)**2 + (ponto_2.Y - ponto_1.Y)**2)


ponto1 = Ponto(1, 2) #x,y
ponto2 = Ponto(4, 6) #x,y

distancia = calcular_distancia(ponto1, ponto2)
print(f"A distância entre {ponto1.X, ponto1.Y} e {ponto2.X, ponto2.Y} é {distancia}")