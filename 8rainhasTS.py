import random
import math

N = 8  # Tamanho do tabuleiro (8x8)

def calcular_conflitos(estado):
    """
    Conta o número de pares de rainhas em conflito no estado fornecido.
    Conflitos acontecem se duas rainhas estão na mesma linha ou na mesma diagonal.
    """
    conflitos = 0
    for i in range(N):
        for j in range(i + 1, N):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                conflitos += 1
    return conflitos

def gerar_estado_vizinho(estado):
    """
    Gera um novo estado alterando a linha de uma rainha aleatória (uma coluna).
    """
    novo_estado = estado[:]
    col = random.randint(0, N - 1)
    nova_linha = random.choice([i for i in range(N) if i != estado[col]])
    novo_estado[col] = nova_linha
    return novo_estado

def simulated_annealing(temp_inicial=200, resfriamento=0.99, temp_minima=0.01):
    """
    Executa o algoritmo de tempera simulada para encontrar uma solução para o problema das 8 rainhas.
    """
    contador = 0
    estado_atual = [random.randint(0, N - 1) for _ in range(N)]
    conflitos_atual = calcular_conflitos(estado_atual)
    temperatura = temp_inicial

    while temperatura > temp_minima and conflitos_atual > 0:
        estado_vizinho = gerar_estado_vizinho(estado_atual)
        conflitos_vizinho = calcular_conflitos(estado_vizinho)

        delta = conflitos_vizinho - conflitos_atual

        # Aceita se for melhor ou com uma certa probabilidade se for pior
        if delta < 0 or random.random() < math.exp(-delta / temperatura):
            estado_atual = estado_vizinho
            conflitos_atual = conflitos_vizinho

        temperatura *= resfriamento
        contador+=1
    if conflitos_atual == 0:
        print("Contador", contador)
        print("Temperatura", temperatura)
        return estado_atual
    else:
        return None

def print_tabuleiro(estado):
    """
    Imprime o tabuleiro de forma visual, com 'R' representando uma rainha.
    """
    for linha in range(N):
        for col in range(N):
            if estado[col] == linha:
                print(" R ", end="")
            else:
                print(" . ", end="")
        print()
    print()

def main():
    print("Executando algoritmo: Tempera Simulada")
    solucao = simulated_annealing()

    if solucao:
        print("Solução encontrada!")
        print("Estado (coluna: linha):", solucao)
        print_tabuleiro(solucao)
    else:
        print("Nenhuma solução foi encontrada.")

if __name__ == "__main__":
    for _ in range(100):
        main()
