# Wumpus World

Este projeto trata-se de um projeto final de disciplina, criado para a disciplina de Inteligência Computacional, que consiste na criação de dois algoritmos, tendo como base o jogo “mundo de Wumpus”. Para este projeto fora criada uma versão a mais do algoritmo reativo, que busca simular a memória após o agente obter o ouro.

> Em todas as pastas, o algoritmo de execução é o **"main.py"**

## **Algoritmo Reativo**

A pasta **"agent"** conta com o algoritmo reativo, onde o agente se move sem levar em conta as percepções, além de não possuir memória. Para usar a flecha fora setada a condição de que seria usada apenas quando o fedor do wumpus fosse sentido, assim o algoritmo gera uma das quatro posições cardinais aleatoriamente para que a flecha seja disparada.

## **Algoritmo Reativo com Memória**

A pasta **"agent_memory"** conta com o algoritmo reativo com memória, seu funcionamento é igual ao do reagente comum, a única mudança foi a adição de uma função que busca simular a memória, essa função é ativada após o agente obter o ouro, usando como base o caminho percorrido para encontrar seu caminho de volta.

## **Algoritmo Genético**

A pasta **"agent_ga"** conta com o algoritmo genético. Isso trata-se de uma tentaviva de implementar o algoritmo genético no mundo de wumpus, buscando encontrar a melhor rota para a obtenção do ouro ao mesmo tempo que evita morrer.
