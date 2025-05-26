Claro! Aqui está um relatório/documentação no formato Markdown (`README.md`) que você pode incluir no seu repositório. Ele explica a implementação do jogo da velha com IA usando o algoritmo **Minimax com poda alfa-beta**, detalha os testes realizados e analisa os ganhos de desempenho da poda.

---


# 🎮 Jogo da Velha com IA (Minimax com Poda Alfa-Beta)

## ✨ Descrição do Projeto

Este projeto é uma implementação do clássico **Jogo da Velha (Tic-Tac-Toe)** com uma interface gráfica feita em **Tkinter**, onde o jogador pode jogar contra uma **IA otimizada com o algoritmo Minimax com Poda Alfa-Beta**.

Além disso, o jogo também oferece a opção de jogar **Humano vs Humano** e permite **alternar entre os modos durante a execução**.

---

## 🧠 Lógica da IA — Minimax com Poda Alfa-Beta

A IA utiliza o algoritmo **Minimax**, uma técnica clássica de inteligência artificial em jogos de dois jogadores. Esse algoritmo simula todas as jogadas possíveis, considerando que o oponente sempre faz a melhor jogada, e escolhe o caminho que leva ao melhor resultado possível.

Para melhorar a performance, usamos **poda Alfa-Beta**, que permite **eliminar ramos da árvore de decisão que não afetam o resultado final**, acelerando o processo sem perda de precisão.

---

## 🖥️ Interface Gráfica

A interface foi construída usando a biblioteca **Tkinter** (inclusa na biblioteca padrão do Python).  
Ela apresenta um tabuleiro 3x3 onde os jogadores podem clicar para jogar, e um botão para **alternar entre modo IA e modo Humano**.

---

## 🔍 Modos de Jogo

- ✅ **Humano vs IA (padrão)**: o jogador "X" joga contra a IA "O".
- ✅ **Humano vs Humano**: dois jogadores se alternam manualmente.
- 🔄 É possível alternar entre os modos com um botão na interface.

---

## 🧪 Testes Realizados: IA vs IA

### Objetivo
Verificar se a IA **toma decisões otimizadas** e **nunca perde** quando joga contra ela mesma.

### Método
Criamos um script onde ambas as jogadas (X e O) são feitas pela IA, utilizando o algoritmo Minimax com poda alfa-beta.

### Resultado
- ✅ **Empate garantido** em todos os jogos.
- ✅ A IA nunca fez uma jogada subótima.
- ✅ O jogo é resolvido rapidamente (em frações de segundo), mesmo com a árvore de possibilidades completa.

---

## 📈 Desempenho: Minimax vs Alfa-Beta

| Algoritmo         | Complexidade        | Avaliações aproximadas | Tempo de resposta |
|-------------------|---------------------|-------------------------|-------------------|
| Minimax puro      | O(b^d)              | Até 362.880 jogadas     | Lento com profundidade alta |
| Minimax + Alfa-Beta | O(b^(d/2)) (melhor caso) | Muito menor              | Quase instantâneo |

### Benefícios da poda alfa-beta:
- ❌ Não avalia ramos que não influenciam o resultado final.
- ⏱️ Reduz consideravelmente o tempo de execução.
- 🧠 Mantém a mesma qualidade de decisão do algoritmo puro.

---

## 📂 Estrutura do Projeto

```


├── jogo\_da\_velha.py        # Código principal com a interface e lógica do jogo   
├── ia\_vs\_ia\_test.py        # Script de teste para IA vs IA  
└── README.md               # Este documento

````

---

## 🚀 Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Execute o arquivo principal:

```bash
  python jogo_da_velha.py
````

3. (Opcional) Para rodar o teste IA vs IA:

```bash
  python ia_vs_ia_test.py
```

---

## 📌 Conclusão

A implementação do Jogo da Velha com IA utilizando **Minimax com Poda Alfa-Beta** é eficiente, jogando perfeitamente e garantindo sempre o melhor resultado. A poda oferece uma melhora de desempenho significativa, mesmo em jogos simples como este, e seria ainda mais essencial em jogos com árvores de decisão maiores.

---