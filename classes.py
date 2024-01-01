'''Ponto:
Atributos: Coordenadas x e y.
Métodos: Distância entre dois pontos, calcular ponto médio.

Reta:
Atributos: Coeficientes a, b e c na equação geral ax+by+c=0.
Métodos: Calcular interseção com outra reta, calcular distância de um ponto à reta.

Círculo:
Atributos: Centro (um ponto) e raio.
Métodos: Calcular área, verificar se um ponto está dentro do círculo.

Funcionalidades:

Operações Básicas com Pontos:
Permita a criação de pontos e realize operações como calcular a distância entre dois pontos e encontrar o ponto médio.

Operações Básicas com Retas:
Permita a criação de retas e realize operações como calcular a interseção entre duas retas e a distância de um ponto a uma reta.

Operações Básicas com Círculos:
Permita a criação de círculos e realize operações como calcular a área do círculo e verificar se um ponto está dentro do círculo.

Interatividade com o Usuário:
Desenvolva uma interface de usuário simples para permitir que o usuário crie pontos, retas e círculos, e realize operações com eles.


Desenvolvimento Adicional:

Visualização Gráfica (Opcional):
Utilize bibliotecas gráficas para criar visualizações gráficas dos pontos, retas e círculos no plano cartesiano.

Persistência de Dados (Opcional):
Implemente a capacidade de salvar e carregar pontos, retas e círculos a partir de arquivos para persistência de dados.

Aplicações Específicas (Opcional):
Adicione funcionalidades específicas, como verificar se duas retas são paralelas, calcular a interseção de uma reta com um círculo, entre outros.'''

class Cartesiano:
    def __init__(self, x, y):
        self.x = x
        self.y= y

class Pontos(Cartesiano):
    def distancia_pontos():
        pass
    def ponto_medio():
        pass

class Reta:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c
    
    def calcular_intercecao()

class Circulo(Cartesiano, raio):
    def __init__(self, x, y, raio):
        super().__init__(x,y)
        self.raio = raio
    
        