import os
from classes import Pontos, Cartesiano, Reta, Circulo

def limpar():
    os.system('cls')

def escolhas():
    valor1x = int(input("x: ")) 
    valor1y = int(input("y: ")) 
    return Cartesiano(valor1x, valor1y)

def coeficientes():
    a = int(input("a: ")) 
    b = int(input("b: ")) 
    return Reta(a, b)

def exibir_menu():
    print("Menu:")
    print("1. Pontos...")
    print("2. Reta...")
    print("3. Circulo...")
    print("4. Sair")

def opcao1():
    print("valor inicial:")
    valor1 = escolhas()
    print("valor final:")
    valor2 = escolhas()
    
    print("1 - Distância entre Pontos...")
    print("2 - Ponto médio...")
    qual = input(":")
    
    if qual == '1':    
        dist = Pontos.distancia_pontos(valor1, valor2)
        print(dist)
    elif qual == '2':
        med = Pontos.ponto_medio(valor1, valor2)
        print(med) 

def opcao2():
    print("1 - Calcular interceção...")
    print("2 - Calcular distância do ponto a reta...")
    qual = input(":")
    if qual == '1':    
        print("primeira equação:")
        valor1 = coeficientes()
        
        print("segunda equação:")
        valor2 = coeficientes()

        ret = Reta.calcular_intercecao(valor1, valor2)
        print(ret)
    elif qual == '2':
        
        print("equação1: ")
        valor1 = coeficientes()
        print("equação2: ")
        valor2 = coeficientes()
        dist= Reta.calcular_distancia_p_r(valor1, valor2)
        print(dist)

def opcao3():
    print("1 - Calcular área...")
    print("2 - Verificar se os pontos estão dentro do circulo...")
    qual = input(":")
    if qual == '1':    
        raio = int(input("raio:"))
        area = Circulo.calcular_area(raio)
        print(area)
    
    elif qual == '2':
        
        raio = int(input("raio:"))
        centro = escolhas()
        valor1 = escolhas()

        ver = Circulo.ponto_dentro(centro, valor1, raio)
        print(ver)
        
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        limpar()
        opcao1()
    elif escolha == '2':
        limpar()
        opcao2()
    elif escolha == '3':
        limpar()
        opcao3()
    elif escolha == '4':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

