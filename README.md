# Otimizador de Horários com Algoritmo Genético

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-concluído-green.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

Um projeto acadêmico que implementa um Algoritmo Genético em Python para resolver o complexo problema de alocação de horários em uma instituição de ensino, buscando uma solução que minimize conflitos.

---

### Tabela de Conteúdos
1. [Descrição do Problema](#1-descrição-do-problema)
2. [A Solução Proposta](#2-a-solução-proposta-algoritmo-genético)
3. [Arquitetura do Código](#3-arquitetura-do-código)
4. [Funcionalidades](#4-funcionalidades)
5. [Tecnologias Utilizadas](#5-tecnologias-utilizadas)

---

### 1. Descrição do Problema

O agendamento de aulas em instituições de ensino é um desafio logístico recorrente. Com dezenas de disciplinas, professores com diferentes disponibilidades, salas limitadas e centenas de alunos matriculados em múltiplas matérias, o número de combinações possíveis para um cronograma torna-se astronomicamente grande. Criar manualmente um horário livre de conflitos é uma tarefa demorada, complexa e sujeita a erros humanos, justificando a necessidade de uma abordagem computacional para encontrar uma solução ótima.

### 2. A Solução Proposta: Algoritmo Genético

Este projeto aborda o desafio utilizando um **Algoritmo Genético**, uma técnica de busca e otimização inspirada na teoria da evolução biológica. O algoritmo simula a "sobrevivência do mais apto" em uma população de soluções candidatas para convergir para uma resposta válida.

Os conceitos fundamentais foram modelados da seguinte forma:

-   **Indivíduo (Cromossomo)**: Representado pela classe `Cronograma`, um indivíduo é uma grade de horários completa, ou seja, uma solução candidata para o problema.
-   **Gene**: Representado pela classe `Aula`, um gene é a menor unidade do nosso cronograma: uma única aula alocada em um professor, sala e horário específicos.
-   **Função de Aptidão (Fitness)**: É o critério que avalia a "qualidade" de um cronograma. Nossa função atribui penalidades severas para cada conflito encontrado (professor, aluno ou sala em duas aulas ao mesmo tempo). Um cronograma perfeito é aquele com **fitness 0**.
-   **Evolução**: Ao longo de centenas de gerações, o algoritmo aplica operadores genéticos:
    -   **Seleção (Torneio)**: Indivíduos melhores (com menos conflitos) são selecionados com maior probabilidade para se tornarem "pais".
    -   **Cruzamento (Ponto Único)**: "Pais" trocam material genético para gerar "filhos", combinando as melhores características das soluções existentes.
    -   **Mutação**: Pequenas alterações aleatórias são introduzidas para garantir diversidade e evitar que o algoritmo fique preso em soluções subótimas.

### 3. Arquitetura do Código

O projeto foi estruturado em múltiplos arquivos para garantir a **separação de responsabilidades**, um princípio fundamental de engenharia de software que torna o código mais limpo, modular e fácil de manter.

```
projeto_horarios/
├── main.py                 # Ponto de entrada, orquestra a execução
├── config.py               # Centraliza todos os dados e parâmetros
├── graphic.py                  # <-- NOVO: Funções de visualização e exportação
│
├── domain/
│   └── models.py           # Define as classes do problema (Professor, Cronograma, etc.)
│
└── genetic_algorithm/
    ├── engine.py           # Contém a classe principal do Algoritmo Genético
    └── factory.py          # Responsável por criar instâncias de Cronograma
```

-   **`config.py`**: Funciona como um painel de controle, onde todos os parâmetros do algoritmo e os dados da instituição podem ser facilmente ajustados.
-   **`domain/models.py`**: É o coração do problema, definindo o que "é" um `Professor`, uma `Aula` e, mais importante, o `Cronograma` com sua lógica interna de cálculo de fitness.
-   **`genetic_algorithm/factory.py`**: Aplica o padrão de projeto *Factory* para encapsular a lógica de criação de indivíduos aleatórios.
-   **`genetic_algorithm/engine.py`**: O motor do projeto. Sua única responsabilidade é executar o ciclo evolutivo. Ele é agnóstico aos detalhes do problema, operando apenas sobre os objetos definidos no domínio.
-   **`main.py`**: O script principal que o usuário executa. Ele amarra todas as partes: carrega a configuração, inicializa o motor e, ao final, processa e apresenta os resultados.

### 4. Funcionalidades

-   [x] Otimização de um cronograma complexo com múltiplos atores e restrições.
-   [x] Logging do progresso no console, mostrando a melhoria do fitness a cada geração.
-   [x] Exportação do melhor cronograma encontrado para um arquivo `cronograma.csv`.
-   [x] Geração e exibição de um gráfico de convergência (`matplotlib`) para análise visual da performance do algoritmo.

### 5. Tecnologias Utilizadas

-   **Python 3.10+**
-   **Matplotlib**