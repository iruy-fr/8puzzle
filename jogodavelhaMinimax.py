import tkinter as tk
from tkinter import messagebox

# --- Lógica do Jogo da Velha ---
def verificar_vencedor(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
            return tabuleiro[0][i]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        return tabuleiro[0][2]

    return None

def jogo_terminou(tabuleiro):
    return verificar_vencedor(tabuleiro) is not None or all(cell != "" for row in tabuleiro for cell in row)

# --- Algoritmo Minimax com poda alfa-beta ---
def minimax(tabuleiro, profundidade, is_max, alpha, beta):
    vencedor = verificar_vencedor(tabuleiro)
    if vencedor == "O":
        return 1
    elif vencedor == "X":
        return -1
    elif jogo_terminou(tabuleiro):
        return 0

    if is_max:
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
                        break
        return melhor
    else:
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
                        break
        return pior

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

# --- Interface Tkinter ---
class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"  # Começa com jogador humano
        self.vs_ia = True  # Modo padrão vs IA

        self.criar_interface()

    def criar_interface(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(3):
            for j in range(3):
                botao = tk.Button(frame, text="", width=5, height=2, font=("Arial", 24),
                                  command=lambda i=i, j=j: self.jogar(i, j))
                botao.grid(row=i, column=j)
                self.botoes[i][j] = botao

        modo_btn = tk.Button(self.root, text="Alternar modo (IA / Humano)", command=self.alternar_modo)
        modo_btn.pack(pady=10)

    def alternar_modo(self):
        self.vs_ia = not self.vs_ia
        modo = "IA" if self.vs_ia else "Humano"
        messagebox.showinfo("Modo de jogo", f"Agora jogando no modo: {modo} vs. Humano")
        self.reiniciar()

    def jogar(self, i, j):
        if self.tabuleiro[i][j] != "" or verificar_vencedor(self.tabuleiro):
            return

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

        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

        if self.vs_ia and self.jogador_atual == "O":
            i_ia, j_ia = melhor_jogada(self.tabuleiro)
            self.root.after(500, lambda: self.jogar(i_ia, j_ia))

    def reiniciar(self):
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text="")
        self.jogador_atual = "X"


# Executar o jogo
if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
