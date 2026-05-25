import numpy as np
import random
import math

PENALIDADE = -999999

def vizinho_aleatorio(estado_atual):
    while True:
        possivel_estado = estado_atual.copy()
        idx = random.choice([0, 1, 2, 3])
        delta = random.choice([1, -1])

        possivel_estado[idx] += delta
        if objetivo(possivel_estado) != PENALIDADE:
            return possivel_estado

def resfriar_temperatura(t):
    # quanto mais lentamente resfriar, melhor a solução, pois vai explorar muito o espaço e salvar o melhor que já passou
    return t * (99.99/100)


def objetivo(solucao):
    a = solucao[0]
    b = solucao[1]
    c = solucao[2]
    d = solucao[3]

    total = (50*a - 1.2*a**2) + (45*b - b**2) + (40*c - 0.8*c**2) + (55*d - 1.5*d**2)

    if (a+b+c+d > 50) or (c+d > 25) or (2*a + b + 3*c + 2*d > 80) or (a < 0 or b < 0 or c < 0 or d < 0):
        return PENALIDADE
    else:
        return total
    

def simulated_annealing():
    estado = np.array([0, 0, 0, 0])
    melhor = estado
    t = 100
    t_min = 0.1
    i = 0

    while t > t_min:
        vizinho = vizinho_aleatorio(estado)

        delta = objetivo(vizinho) - objetivo(estado)

        if delta > 0:
            estado = vizinho
        elif random.random() < math.exp(delta/t):
            estado = vizinho

        if objetivo(estado) > objetivo(melhor):
            melhor = estado

        t = resfriar_temperatura(t)
        i += 1
    
    print(f"iteracoes: {i}")
    return melhor
    
        
if __name__ == "__main__":
    solucao = simulated_annealing()

    print("Melhor estado encontrado: ", solucao, "lucro total: ", objetivo(solucao))

# Melhor estado encontrado:  [12 17  5 12] lucro total:  1527.2 - (0.9999 cooling rate)