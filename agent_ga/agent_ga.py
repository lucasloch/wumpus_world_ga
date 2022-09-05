from action import Action, table_of_actions
from map import Map
from random import random, randrange, choice


class Agent(object):
    def __init__(self, mapa: Map, dimension_map: int, geracao=0):
        self.dimension = dimension_map
        self.mapa = mapa
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []
        if self.geracao == 0:
            n_moves = randrange(dimension_map**2+2, 100)
            actions = list(table_of_actions.keys())
            for _ in range(n_moves):
                move = choice(actions)
                if move == '':
                    self.cromossomo.append('K')
                else:
                    self.cromossomo.append(move)

    def avaliacao(self):
        nota = 0
        weights = [
            1000,  # has gold
            70,  # 500,  # win
            500,  # 200,  # kill wumpus
            -1,  # move
            -2,  # move dumb
            -10,  # -200  # death
        ]
        nota_aval = self.agPlay()
        for i in range(len(nota_aval)):
            nota += nota_aval[i] * weights[i]
        self.nota_avaliacao = nota

    def moveAction(self, actual: tuple, move) -> tuple:
        x, y = actual
        if move == 'N':
            x -= 1
        if move == 'S':
            x += 1
        if move == 'E':
            y += 1
        if move == 'W':
            y -= 1
        return x, y

    def shooAction(self, actual: tuple, move):
        x, y = actual
        if move == 'Z':
            x -= 1
        if move == 'X':
            x += 1
        if move == 'C':
            y += 1
        if move == 'V':
            y -= 1
        return x, y

    def agPlay(self):
        has_gold = False
        agent_win = False
        wumpus_killed = False
        has_arrow = True
        qtd_actions = 0
        dumb_actions = 0
        agent_death = False
        local_atual = (0, 0)
        moves_accepts = []
        mapa = self.mapa
        new_local = local_atual

        for i in range(len(self.cromossomo)):
            dumb = False
            qtd_actions += 1

            # Verifica se é 'ouro'
            if self.cromossomo[i] == 'K':
                if mapa[local_atual[0]][local_atual[1]] == 'gold' and has_gold is False:
                    has_gold = True
                else:
                    dumb = True
                    dumb_actions += 1
            # Verifica se é atirar
            elif self.cromossomo[i] in ['Z', 'X', 'C', 'V'] and has_arrow:
                shoot_direction = self.shooAction(local_atual, self.cromossomo[i])
                if shoot_direction[0] < 0 or shoot_direction[0] > self.dimension - 1 or shoot_direction[1] < 0 or shoot_direction[1] > self.dimension - 1:
                    dumb = True
                    dumb_actions += 1
                    has_arrow = False
                elif mapa[shoot_direction[0]][shoot_direction[1]] == 'wumpus':
                    wumpus_killed = True
                    has_arrow = False
                else:
                    dumb = True
                    dumb_actions += 1
                    has_arrow = False
            # Verifica se é mover
            else:
                new_local = self.moveAction(local_atual, self.cromossomo[i])
                # Verifica se ta fora do mapa
                if new_local[0] < 0 or new_local[0] > self.dimension-1 or new_local[1] < 0 or new_local[1] > self.dimension - 1:
                    dumb = True
                    dumb_actions += 1
                # Verifica se morreu
                elif mapa[new_local[0]][new_local[1]] in ['wumpus', 'pit']:
                    # print(self.mapa.matrix[local_atual[0]][local_atual[1]])
                    dumb = True
                    dumb_actions += 1
                    agent_death = True
                # Verifica se escapou
                # elif new_local == (0, 0) and qtd_actions > 5:
                    # agent_win = True

            if agent_death:
                break

            if dumb is False:
                moves_accepts.append(self.cromossomo[i])

            # Verifica se venceu
            if new_local == (0, 0) and has_gold:
                break

            local_atual = new_local

        # self.cromossomo = moves_accepts
        # print(moves_accepts)
        return [has_gold, agent_win, wumpus_killed, qtd_actions, dumb_actions, agent_death]

    def crossover(self, outro_agent, mapa: Map):
        corte = round(random() * len(self.cromossomo))
        # print(f'corte: {corte}')

        filho1 = outro_agent.cromossomo[0:corte] + self.cromossomo[corte::]
        # print(f'filho1: {filho1}')
        filho2 = self.cromossomo[0:corte] + outro_agent.cromossomo[corte::]
        # print(f'filho2: {filho2}')

        filhos = [Agent(mapa, self.dimension, self.geracao + 1),
                  Agent(mapa, self.dimension, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos

    def mutacao(self, taxa_mutacao):
        # print(f"Antes {self.cromossomo}")
        actions = list(table_of_actions.keys())
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                self.cromossomo[i] = choice(['N', 'S', 'E', 'W'])
        # print(f"Depois {self.cromossomo}\n")
        return self


class AlgoritmoGenetico(object):
    def __init__(self, tamanho_populacao: int, mapa: Map, dimension: int):
        self.mapa = mapa.matrix
        self.dimension = dimension
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []
        self.countPai = 0

    def inicializa_populacao(self):
        mapa = self.mapa
        for i in range(self.tamanho_populacao):
            self.populacao.append(Agent(mapa, self.dimension))
        self.melhor_solucao = self.populacao[0]

    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key=lambda populacao: populacao.nota_avaliacao and len(populacao.cromossomo) > 2,
                                reverse=True)

    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo

    def seleciona_pai(self):
        if self.countPai == len(self.populacao):
            self.countPai = 0
        pai = self.countPai
        self.countPai += 1
        return pai

    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print(f"G:{self.populacao[0].geracao} -> Pontuação: {melhor.nota_avaliacao} Cromossomo: {melhor.cromossomo}")

    def getNewPopulation(self):
        population = self.populacao[0:int(self.tamanho_populacao * 0.1)]
        for i in range(len(population)):
            if len(population[i].cromossomo) < 1:
                population[i] = population[0]
        return population

    def resolver(self, taxa_mutacao, numero_geracoes):
        self.inicializa_populacao()

        for individuo in self.populacao:
            individuo.avaliacao()

        self.ordena_populacao()
        self.melhor_solucao = self.populacao[0]
        self.populacao = self.getNewPopulation()
        self.visualiza_geracao()

        for geracao in range(numero_geracoes):
            nova_populacao = []

            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai()
                pai2 = self.seleciona_pai()

                filhos = self.populacao[pai1].crossover(self.populacao[pai2], self.mapa)

                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
                # print(f'pai {individuos_gerados}: {self.populacao[pai1].cromossomo}')
                # print(f'pai {individuos_gerados+1}: {self.populacao[pai2].cromossomo}')
                # print(f'filho 1: {filhos[0].cromossomo}')
                # print(f'filho 2: {filhos[1].cromossomo}')

            self.populacao = list(nova_populacao)

            for individuo in self.populacao:
                individuo.avaliacao()

            self.ordena_populacao()
            self.visualiza_geracao()
            melhor = self.populacao[0]
            self.populacao = self.getNewPopulation()
            self.lista_solucoes.append(melhor.nota_avaliacao)
            self.melhor_individuo(melhor)

        print(f"\nMelhor solução -> G:{self.melhor_solucao.geracao} -> Pontuação: {self.melhor_solucao.nota_avaliacao} Cromossomo: {self.melhor_solucao.cromossomo}")

        return self.melhor_solucao.cromossomo


if __name__ == '__main__':
    mapa1 = Map(4)
    eva = Agent(mapa1, 4)
    adao = Agent(mapa1, 4)
    cromossomo = [choice(list(table_of_actions.keys()))]
    filho = eva.crossover(adao)
    print(eva.cromossomo)
    print(adao.cromossomo)
    print(filho[0].cromossomo)
    print(filho[1].cromossomo)
