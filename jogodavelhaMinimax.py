import tkinter as tk
from tkinter import messagebox


# --- Lógica do Jogo da Velha ---

# Verifica se há um vencedor no tabuleiro atual
def verificar_vencedor(tabuleiro):
    # Verifica linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
            return tabuleiro[0][i]

    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        return tabuleiro[0][2]

    return None  # Ninguém venceu ainda


# Verifica se o jogo terminou (vitória ou empate)
def jogo_terminou(tabuleiro):
    return verificar_vencedor(tabuleiro) is not None or all(cell != "" for row in tabuleiro for cell in row)


# --- Algoritmo Minimax com poda alfa-beta ---

# Função recursiva para avaliar as jogadas possíveis e retornar o melhor valor
def minimax(tabuleiro, profundidade, is_max, alpha, beta):
    vencedor = verificar_vencedor(tabuleiro)
    if vencedor == "O":  # IA venceu
        return 1
    elif vencedor == "X":  # Jogador humano venceu
        return -1
    elif jogo_terminou(tabuleiro):  # Empate
        return 0

    if is_max:  # Turno da IA (maximizador)
        melhor = -float("inf")
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == "":
                    tabuleiro[i][j] = "O"
                    valor = minimax(tabuleiro, profundidade + 1, False, alpha, beta)
                    tabuleiro[i][j] = ""
                    melhor = max(melhor, valor)
                    alpha = max(alpha, valor)
                    if beta <= alpha:
                        break  # Poda beta
        return melhor
    else:  # Turno do jogador humano (minimizador)
        pior = float("inf")
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == "":
                    tabuleiro[i][j] = "X"
                    valor = minimax(tabuleiro, profundidade + 1, True, alpha, beta)
                    tabuleiro[i][j] = ""
                    pior = min(pior, valor)
                    beta = min(beta, valor)
                    if beta <= alpha:
                        break  # Poda alfa
        return pior


# Encontra a melhor jogada para a IA utilizando o Minimax
def melhor_jogada(tabuleiro):
    melhor_valor = -float("inf")
    jogada = (-1, -1)
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == "":
                tabuleiro[i][j] = "O"
                valor = minimax(tabuleiro, 0, False, -float("inf"), float("inf"))
                tabuleiro[i][j] = ""
                if valor > melhor_valor:
                    melhor_valor = valor
                    jogada = (i, j)
    return jogada


# --- Interface Gráfica com Tkinter ---

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        # Tabuleiro lógico: 3x3 inicialmente vazio
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]

        # Referência aos botões da interface
        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        # Jogador atual (X começa)
        self.jogador_atual = "X"

        # Modo de jogo: True = Humano vs IA; False = Humano vs Humano
        self.vs_ia = True

        # Cria a interface gráfica do jogo
        self.criar_interface()

    def criar_interface(self):
        frame = tk.Frame(self.root)
        frame.pack()

        # Cria os 9 botões do tabuleiro (3x3)
        for i in range(3):
            for j in range(3):
                botao = tk.Button(frame, text="", width=5, height=2, font=("Arial", 24),
                                  command=lambda i=i, j=j: self.jogar(i, j))
                botao.grid(row=i, column=j)
                self.botoes[i][j] = botao

        # Botão para alternar entre os modos de jogo
        modo_btn = tk.Button(self.root, text="Alternar modo (IA / Humano)", command=self.alternar_modo)
        modo_btn.pack(pady=10)

    def alternar_modo(self):
        # Alterna entre Humano vs Humano e Humano vs IA
        self.vs_ia = not self.vs_ia
        modo = "IA" if self.vs_ia else "Humano"
        messagebox.showinfo("Modo de jogo", f"Agora jogando no modo: {modo} vs. Humano")
        self.reiniciar()

    def jogar(self, i, j):
        # Impede jogada se a célula já estiver preenchida ou se o jogo já tiver terminado
        if self.tabuleiro[i][j] != "" or verificar_vencedor(self.tabuleiro):
            return

        # Marca o tabuleiro e atualiza a interface
        self.tabuleiro[i][j] = self.jogador_atual
        self.botoes[i][j].config(text=self.jogador_atual)

        vencedor = verificar_vencedor(self.tabuleiro)
        if vencedor:
            messagebox.showinfo("Fim de jogo", f"Jogador {vencedor} venceu!")
            self.reiniciar()
            return

        if jogo_terminou(self.tabuleiro):
            messagebox.showinfo("Fim de jogo", "Empate!")
            self.reiniciar()
            return

        # Alterna jogador
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

        # Se for IA, ela faz a jogada
        if self.vs_ia and self.jogador_atual == "O":
            i_ia, j_ia = melhor_jogada(self.tabuleiro)
            self.root.after(500, lambda: self.jogar(i_ia, j_ia))  # IA joga com leve atraso para parecer mais natural

    def reiniciar(self):
        # Limpa o tabuleiro e interface para reinício de partida
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text="")
        self.jogador_atual = "X"  # Sempre começa com X


# --- Execução principal do jogo ---
if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()