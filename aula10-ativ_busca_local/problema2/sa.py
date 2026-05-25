import numpy as np
import random
import math

PENALIDADE = -999999

def vizinho_aleatorio(estado_atual):
    while True:
        possivel_estado = estado_atual.copy()
        delta = random.choice([0.01, -0.01])

        possivel_estado[0] += delta
        if objetivo(possivel_estado) != PENALIDADE:
            # print(possivel_estado)
            return possivel_estado

def resfriar_temperatura(t):
    # quanto mais lentamente resfriar, melhor a solução, pois vai explorar muito o espaço e salvar o melhor que já passou
    return t * (99.999/100)


def objetivo(solucao):
    a = solucao[0]

    total = a * math.sin(10*math.pi*a) + 1

    if a < -1 or a > 2:
        return PENALIDADE
    else:
        return total
    

def simulated_annealing():
    estado = np.array([0.0])
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

        # Dentro do loop while do SA:
        # print(f"Atual: {objetivo(estado)} | Candidato: {objetivo(vizinho)} | Delta: {delta}")
    
    print(f"iteracoes: {i}")
    return melhor
    
        
if __name__ == "__main__":
    solucao = simulated_annealing()

    print("Melhor estado encontrado: ", solucao, "ponto máximo: ", objetivo(solucao))

# Melhor estado encontrado:  [1.85] ponto máximo:  2.8500000000000014 - (0.99999 cooling rate) - passo de 0.01/-0.01