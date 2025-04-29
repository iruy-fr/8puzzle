from collections import deque

def ler_arquivo_para_matriz(entrada):
    with open(entrada, 'r') as arquivo:
        linhas = arquivo.readlines()

    estado_inicial = []
    for linha in linhas:
        numeros = linha.strip().split()  # Remove espaços e quebras de linha, depois separa por espaço
        linha_inteiros = [int(num) for num in numeros]
        estado_inicial.append(linha_inteiros)

    return estado_inicial


# Função BFS para o 8-puzzle (igual à anterior)
def bfs_8puzzle(estado_inicial):
    objetivo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    if estado_inicial == objetivo:
        return [estado_inicial]

    fila = deque()
    fila.append((estado_inicial, []))
    visitados = set()
    visitados.add(tuple(map(tuple, estado_inicial)))

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while fila:
        estado_atual, caminho = fila.popleft()

        # Encontra a posição do 0
        for i in range(3):
            for j in range(3):
                if estado_atual[i][j] == 0:
                    x, y = i, j
                    break

        # Gera novos estados
        for dx, dy in direcoes:
            novo_x, novo_y = x + dx, y + dy
            if 0 <= novo_x < 3 and 0 <= novo_y < 3:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[x][y], novo_estado[novo_x][novo_y] = novo_estado[novo_x][novo_y], novo_estado[x][y]

                if tuple(map(tuple, novo_estado)) not in visitados:
                    if novo_estado == objetivo:
                        return caminho + [novo_estado]
                    visitados.add(tuple(map(tuple, novo_estado)))
                    fila.append((novo_estado, caminho + [novo_estado]))

    return None


# Função para imprimir o estado
def imprimir_estado(estado):
    for linha in estado:
        print(" ".join(map(str, linha)))
    print()


# Exemplo de uso
if __name__ == "__main__":
    entrada = "entrada.txt"  # Substitua pelo nome do seu arquivo
    estado_inicial = ler_arquivo_para_matriz(entrada)

    print("=== Estado Inicial (Lido do Arquivo) ===")
    imprimir_estado(estado_inicial)

    solucao = bfs_8puzzle(estado_inicial)

    if solucao:
        print(f"=== Solução em {len(solucao)} movimentos ===")
        for i, estado in enumerate(solucao):
            print(f"Movimento {i}:")
            imprimir_estado(estado)
    else:
        print("Não há solução para este estado.")