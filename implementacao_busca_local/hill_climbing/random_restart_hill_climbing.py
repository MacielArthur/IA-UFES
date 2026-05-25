import numpy as np

PENALIDADE = -999999

def solucao_inicial():
    while True:
        solucao = np.array(np.random.randint(0, 20, size=3))
        if objetivo(solucao) != PENALIDADE:
            return solucao

def gerar_vizinhos(estado_atual):
    estado = estado_atual.copy()

    vizinhos = []
    vizinhos.append([estado[0]+1, estado[1], estado[2]])
    vizinhos.append([estado[0]-1, estado[1], estado[2]])
    vizinhos.append([estado[0], estado[1]+1, estado[2]])
    vizinhos.append([estado[0], estado[1]-1, estado[2]])
    vizinhos.append([estado[0], estado[1], estado[2]+1])
    vizinhos.append([estado[0], estado[1], estado[2]-1])

    return np.array(vizinhos)

def melhor_vizinho(estado_atual):
    vizinhos = gerar_vizinhos(estado_atual)

    objetivo_vizinhos = np.apply_along_axis(objetivo, 1, vizinhos)
    melhor_idx = np.argmax(objetivo_vizinhos)

    return vizinhos[melhor_idx]

def objetivo(solucao):
    a = solucao[0]
    b = solucao[1]
    c = solucao[2]

    total = 30*a + 50*b + 40*c

    if 2*a + 4*b + 3*c > 100 or 3*a + 2*b + 4*c > 90 or a < 0 or b < 0 or c < 0:
        return PENALIDADE
    else:
        return total
    

def random_restart_hill_climbing():
    estado_atual = solucao_inicial()

    while True:
        vizinho = melhor_vizinho(estado_atual)

        if objetivo(vizinho) <= objetivo(estado_atual):
            return estado_atual

        estado_atual = vizinho
    
        
if __name__ == "__main__":
    solucoes = []

    for _ in range(300):
        solucoes.append(random_restart_hill_climbing())
    
    solucoes = np.array(solucoes)

    obj_solucoes = np.apply_along_axis(objetivo, 1, solucoes)
    melhor_idx = np.argmax(obj_solucoes)

    print("Melhor estado encontrado: ", solucoes[melhor_idx], "lucro total: ", obj_solucoes[melhor_idx])
