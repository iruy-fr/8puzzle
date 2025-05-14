import heapq


def ler_arquivo_para_matriz(entrada):
    with open(entrada, 'r') as arquivo:
        linhas = arquivo.readlines()

    estado_inicial = []
    for linha in linhas:
        numeros = linha.strip().split()
        linha_inteiros = [int(num) for num in numeros]
        estado_inicial.append(linha_inteiros)

    return estado_inicial


# Função para calcular a distância de Manhattan
def distancia_manhattan(estado, objetivo):
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = estado[i][j]
            if valor != 0:
                for x in range(3):
                    for y in range(3):
                        if objetivo[x][y] == valor:
                            distancia += abs(x - i) + abs(y - j)
    return distancia


# Função para verificar se o 8-puzzle é solucionável
def soluvel(estado):
    # Transformar a matriz em uma lista 1D, ignorando o 0
    lista = [num for linha in estado for num in linha if num != 0]

    inversoes = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                inversoes += 1

    return inversoes % 2 == 0


# Função A* para o 8-puzzle
def astar_8puzzle(estado_inicial):
    objetivo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    if estado_inicial == objetivo:
        return [estado_inicial]

    fila = []
    heapq.heappush(fila, (distancia_manhattan(estado_inicial, objetivo), 0, estado_inicial, []))
    visitados = set()
    visitados.add(tuple(map(tuple, estado_inicial)))

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while fila:
        custo_total, movimentos, estado_atual, caminho = heapq.heappop(fila)

        # Encontra a posição do 0
        for i in range(3):
            for j in range(3):
                if estado_atual[i][j] == 0:
                    x, y = i, j
                    break
            else:
                continue
            break  # Sai do laço externo também

        # Explora os movimentos possíveis a partir do 0
        for dx, dy in direcoes:
            novo_x, novo_y = x + dx, y + dy
            if 0 <= novo_x < 3 and 0 <= novo_y < 3:
                # Cria uma cópia do estado atual pra depois inserir o novo estado
                novo_estado = []
                for linha in estado_atual:
                    nova_linha = []
                    for elemento in linha:
                        nova_linha.append(elemento)
                    novo_estado.append(nova_linha)

                #Troca as posições do 0 com o número vizinho
                novo_estado[x][y], novo_estado[novo_x][novo_y] = novo_estado[novo_x][novo_y], novo_estado[x][y]

                novo_estado_tupla = tuple(map(tuple, novo_estado))
                if novo_estado_tupla in visitados:
                    continue

                visitados.add(novo_estado_tupla)
                novo_movimentos = movimentos + 1
                heuristica = distancia_manhattan(novo_estado, objetivo)

                if novo_estado == objetivo:
                    return caminho + [novo_estado]

                heapq.heappush(fila, (
                    novo_movimentos + heuristica,
                    novo_movimentos,
                    novo_estado,
                    caminho + [novo_estado]
                ))


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

    if not soluvel(estado_inicial):
        print("Este 8-puzzle é impossível de resolver.")
    else:
        solucao = astar_8puzzle(estado_inicial)

        if solucao:
            print(f"=== Solução em {len(solucao)} movimentos ===")
            for i, estado in enumerate(solucao):
                print(f"Movimento {i + 1}:")
                imprimir_estado(estado)
        else:
            print("Não há solução encontrada.")
