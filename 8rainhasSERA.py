import random

N = 8  # Número de rainhas


def gerar_estado_aleatorio():
    """Gera uma configuração aleatória onde cada rainha está em uma coluna diferente."""
    return [random.randint(0, N - 1) for _ in range(N)]


def contar_conflitos(estado):
    """Conta o número de pares de rainhas em conflito."""
    conflitos = 0
    for i in range(N):
        for j in range(i + 1, N):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                conflitos += 1
    return conflitos


def vizinho_com_menor_conflito(estado):
    """Gera o melhor vizinho possível movendo uma rainha de cada vez."""
    melhor_estado = estado[:]
    menor_conflito = contar_conflitos(estado)

    for col in range(N):
        estado_original = estado[col]
        for linha in range(N):
            if linha != estado_original:
                estado[col] = linha
                conflitos = contar_conflitos(estado)
                if conflitos < menor_conflito:
                    menor_conflito = conflitos
                    melhor_estado = estado[:]
        estado[col] = estado_original  # volta ao estado original

    return melhor_estado, menor_conflito


def subida_de_encosta_com_reinicio(max_reinicios=1000):
    """Executa a subida de encosta com reinício aleatório."""
    reinicios = 0
    passos = 0

    while reinicios < max_reinicios:
        estado = gerar_estado_aleatorio()
        conflitos = contar_conflitos(estado)

        while True:
            novo_estado, novo_conflitos = vizinho_com_menor_conflito(estado)
            passos += 1

            if novo_conflitos == 0:
                return novo_estado, passos, reinicios

            if novo_conflitos >= conflitos:
                break  # chegou a um ótimo local, reiniciar

            estado = novo_estado
            conflitos = novo_conflitos

        reinicios += 1

    return None, passos, reinicios  # se não encontrou solução


def print_tabuleiro(estado):
    """Imprime o tabuleiro com rainhas baseadas na configuração fornecida."""
    for linha in range(N):
        linha_str = ""
        for col in range(N):
            if estado[col] == linha:
                linha_str += " R "
            else:
                linha_str += " . "
        print(linha_str)
    print()


# Executa o algoritmo
if __name__ == "__main__":
    solucao, passos, reinicios = subida_de_encosta_com_reinicio()

    if solucao:
        print("Solução encontrada:")
        print(solucao)
        print("Conflitos:", contar_conflitos(solucao))
        print("Passos:", passos)
        print("Reinícios:", reinicios)
        print_tabuleiro(solucao)
    else:
        print("Nenhuma solução encontrada após o número máximo de reinícios.")
