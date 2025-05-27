## 🧠 **Relatório Comparativo — Solução do Problema das 8 Rainhas**

---

### 1. **Abordagem Teórica de Cada Algoritmo**

#### 🔬 **Algoritmo Genético**

Baseado nos princípios da seleção natural. Uma população de soluções evolui ao longo de gerações por meio de seleção, cruzamento e mutação. O objetivo é minimizar o número de conflitos entre rainhas.

#### 🔄 **Subida de Encosta com Reinício Aleatório**

Algoritmo local que busca melhorar incrementalmente uma solução inicial, escolhendo vizinhos com menos conflitos. Em caso de platôs ou mínimos locais, reinicia a busca a partir de um novo estado aleatório.

#### ❄️ **Tempera Simulada**

Inspirado no processo físico de recozimento. O algoritmo aceita soluções piores com uma certa probabilidade que diminui ao longo do tempo (temperatura), permitindo escapar de mínimos locais.

---

### 2. **Implementação Prática**

* **Representação da Solução**: Todos os algoritmos representaram o estado como uma lista de 8 inteiros (1 por coluna), indicando a linha de cada rainha.
* **Critério de Avaliação**: Número de pares de rainhas em conflito (mesma linha ou mesma diagonal).
* **Critério de Parada**:

  * Genético: número máximo de gerações ou solução encontrada.
  * Subida de Encosta: número máximo de reinícios ou solução encontrada.
  * Tempera Simulada: temperatura mínima ou solução encontrada.
* **Execuções**: Cada algoritmo foi executado 100 vezes para fins de comparação estatística.
  
  * Genético: testes feitos com número máximo de 1000,1500 e 2000 gerações ou solução encontrada.
  * Subida de Encosta: testes feitos com número máximo de 100, 500 e 1000 reinícios.
  * Tempera Simulada: testes feitos com temperatura mínima de ou solução encontrada.

---

### 3. **Resultados Obtidos (300 Execuções por Algoritmo com diferentes valores)**

| 🔢 **Métrica**               | 🧬 Genético | 🧗 Subida c/ Reinício | ❄️ Tempera Simulada |
| ---------------------------- |-------------|-----------------------|---------------------|
| ✅ **Taxa de Sucesso (%)**    | 71%         | 100%                  | 36%                 |
| 🔁 **Média de Iterações**    | 237.64      | 34.51                 | 258.73              |
| ⏱ **Tempo Médio (segundos)** | 0.0033      | 0.0194                | 0.0083              |
| ❌ **Erro Médio (se falhou)** | 2.0         | 0.07                  | 0.11                |

> Nota: Iterações correspondem a soma das gerações divididas por 300 (genético), soma da quantidade de passos divididos por 300 (subida de encosta) 
> ou quantidade de ciclos até o resultado ou resfriamento final (tempera simulada).

---

### 4. **Discussão: Vantagens e Desvantagens**

#### ✅ **Genético**

* **Vantagens**:

  * Extremamente rápido.
  * Robusto a ruído e múltiplas soluções possíveis.
* **Desvantagens**:

  * Menor taxa de sucesso.
  * Pode convergir prematuramente se a diversidade da população for baixa.

#### ✅ **Subida de Encosta com Reinício Aleatório**

* **Vantagens**:

  * Maior taxa de sucesso (99%).
  * Simples e eficiente para este problema específico.
* **Desvantagens**:

  * Alto número de iterações.
  * Pode ser ineficiente para problemas com espaços de busca maiores.

#### ✅ **Tempera Simulada**

* **Vantagens**:

  * Boa taxa de sucesso.
  * Capacidade de escapar de ótimos locais.
* **Desvantagens**:

  * Mais sensível à parametrização (temperatura inicial e fator de resfriamento).
  * Levemente mais lento que o genético.

---

### 5. **Conclusão: Qual o Mais Eficiente?**

Com base nos resultados empíricos:

* **Mais eficiente (desempenho geral)**: **Subida de Encosta com Reinício Aleatório**

  * Melhor taxa de sucesso e erro quase nulo.
* **Mais rápido**: **Algoritmo Genético**

  * Ideal para aplicações onde a velocidade é mais crítica que a garantia de sucesso.
* **Mais equilibrado**: **Tempera Simulada**

  * Boa combinação entre qualidade da solução e tempo de execução.

✅ **Escolha recomendada**:
Para aplicações práticas no problema das 8 rainhas, a **Subida de Encosta com Reinício Aleatório** se destaca como a abordagem mais **eficaz e confiável**.

---