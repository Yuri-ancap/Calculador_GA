import math
class Cartesiano:
    
    def __init__(self, x=0, y=0):
        self._x = x
        self._y= y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Pontos(Cartesiano):
    def distancia_pontos(ponto2, ponto1):
        resposta = ((ponto1.x - ponto2.x)**2 + (ponto1.y - ponto2.y)**2)**(1/2)
        return f'distancia = {resposta}'
        
    def ponto_medio(ponto2, ponto1):
        valory = (ponto2.x - ponto1.x)/2
        valorx = (ponto2.y - ponto1.y)/2

        return f'x={valorx} e y={valory} são os pontos médios'

class Reta:
    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b 

    @property
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b
    

    def calcular_intercecao(valor2, valor1):
        if valor2.a == valor1.a:
            return f'não se interceptam'   
        else:
            x = (valor1.b - valor2.b)/(valor2.a - valor1.a )
            y = valor1.a*x + valor1.b
            return f'x={x} y={y} são os pontos de intersecção' 
        
    def calcular_distancia(valor2, valor1):
        if valor2.a != valor1.a:
            return f'distancia não existe'
        else:
            return abs((valor2.b - valor1.b)/((1 + valor1.a**(2)))**(1/2))

class Circulo(Cartesiano):
    def __init__(self, x, y, raio):
       super().__init__(x,y)
       self._raio = raio
    
    @property
    def raio(self):
        return self._raio
    
    def calcular_area(raio):
        return math.pi* raio * raio 
        
    def ponto_dentro(centro, coordenadas, raio):
        if centro.y + raio >= coordenadas.y and centro.x + raio >= coordenadas.x:
            return f'{coordenadas.x} e {coordenadas.y} estão dentro do círculo!'
        else:
            return f'{coordenadas.x} e {coordenadas.y} Não pertencem ao círculo!'
 