import random

N = 8  # Tamanho do tabuleiro (8x8)
TAMANHO_POPULACAO = 100
TAXA_MUTACAO = 0.05
MAX_GERACOES = 1000

def criar_individuo():
    """Gera uma solução aleatória (1 rainha por coluna, em linha aleatória)."""
    return [random.randint(0, N - 1) for _ in range(N)]

def calcular_conflitos(estado):
    """Conta o número de pares de rainhas em conflito."""
    conflitos = 0
    for i in range(N):
        for j in range(i + 1, N):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                conflitos += 1
    return conflitos

def selecao(populacao):
    """Seleciona dois indivíduos com base na roleta (quanto menos conflitos, maior chance)."""
    populacao.sort(key=calcular_conflitos)
    return populacao[0], populacao[1]  # Elite selection (melhores dois)

def crossover(pai1, pai2):
    """Cruzamento entre dois pais para gerar um filho."""
    ponto = random.randint(0, N - 1)
    filho = pai1[:ponto] + pai2[ponto:]
    return filho

def mutacao(individuo):
    """Aplica mutação em uma posição aleatória."""
    if random.random() < TAXA_MUTACAO:
        coluna = random.randint(0, N - 1)
        nova_linha = random.randint(0, N - 1)
        individuo[coluna] = nova_linha
    return individuo

def genetico_8rainhas():
    """Executa o algoritmo genético para encontrar uma solução."""
    populacao = [criar_individuo() for _ in range(TAMANHO_POPULACAO)]

    for geracao in range(MAX_GERACOES):
        nova_populacao = []

        for _ in range(TAMANHO_POPULACAO):
            pai1, pai2 = selecao(populacao)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho)
            nova_populacao.append(filho)

            if calcular_conflitos(filho) == 0:
                return filho, geracao + 1

        populacao = nova_populacao

    return None, MAX_GERACOES

def print_tabuleiro(estado):
    """Imprime o tabuleiro de forma visual."""
    for linha in range(N):
        for col in range(N):
            if estado[col] == linha:
                print(" R ", end="")
            else:
                print(" . ", end="")
        print()
    print()

def main():
    print("Executando algoritmo: Algoritmo Genético")
    solucao, geracoes = genetico_8rainhas()

    if solucao:
        print(f"Solução encontrada em {geracoes} gerações!")
        print("Estado (coluna: linha):", solucao)
        print_tabuleiro(solucao)
    else:
        print("Nenhuma solução foi encontrada após o limite de gerações.")

if __name__ == "__main__":
    main()
