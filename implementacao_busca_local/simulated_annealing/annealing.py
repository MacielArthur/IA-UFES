import numpy as np
import random
import math

PENALIDADE = -999999

def vizinho_aleatorio(estado_atual):
    while True:
        possivel_estado = estado_atual.copy()
        idx = random.choice([0, 1, 2])
        delta = random.choice([1, -1])

        possivel_estado[idx] += delta
        if objetivo(possivel_estado) != PENALIDADE:
            return possivel_estado

def resfriar_temperatura(t):
    # quanto mais lentamente resfriar, melhor a solução, pois vai explorar muito o espaço e salvar o melhor que já passou
    return t * (99/100)


def objetivo(solucao):
    a = solucao[0]
    b = solucao[1]
    c = solucao[2]

    total = 30*a + 50*b + 40*c

    if 2*a + 4*b + 3*c > 100 or 3*a + 2*b + 4*c > 90 or a < 0 or b < 0 or c < 0:
        return PENALIDADE
    else:
        return total
    

def simulated_annealing():
    estado = np.array([0, 0, 0])
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
