from agent_ga import AlgoritmoGenetico as AgentGA
from map_ga import MapGA as Map
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dimension_map = 4
    mapa = Map(dimension_map, map_fix=True)
    mapa.printMatrix((0, 0))
    tamanho_populacao = 20
    taxa_mutacao = 0.01
    numero_geracoes = 100

    ag = AgentGA(tamanho_populacao, mapa, dimension_map)
    resultado = ag.resolver(taxa_mutacao, numero_geracoes)

    # JOGANDO
    local_atual = (0, 0)
    scream = False
    gold = False
    arrow = True
    death = False
    out = False
    tiro = False

    # Testar os movimentos escolhidos
    for i in range(len(resultado)):
        out = False
        tiro = False
        shoot_direction = local_atual
        new_local = (0, 0)
        # Verifica se é 'ouro'
        if resultado[i] == 'K':
            if mapa.matrix[local_atual[0]][local_atual[1]] == 'gold' and gold is False:
                gold = True
        # Verifica se é atirar
        elif resultado[i] in ['Z', 'X', 'C', 'V'] and arrow:
            tiro = True
            if resultado[i] == 'Z':
                shoot_direction = (shoot_direction[0] - 1, shoot_direction[1])
            elif resultado[i] == 'X':
                shoot_direction = (shoot_direction[0] + 1, shoot_direction[1])
            elif resultado[i] == 'C':
                shoot_direction = (shoot_direction[0], shoot_direction[1] + 1)
            elif resultado[i] == 'V':
                shoot_direction = (shoot_direction[0], shoot_direction[1] - 1)
            if shoot_direction[0] < 0 or shoot_direction[0] > dimension_map - 1 or shoot_direction[1] < 0 or \
                    shoot_direction[1] > dimension_map - 1:
                print('EROOOOOOOU!!')
                arrow = False
            elif mapa.matrix[shoot_direction[0]][shoot_direction[1]] == 'wumpus':
                scream = True
                print('FALICEU! DANÇA GATINHO, DANÇA!')
            else:
                print('EROOOOOOOU!!')
                arrow = False
        # Verifica se é mover
        else:
            if resultado[i] == 'N':
                new_local = (local_atual[0] - 1, local_atual[1])
            elif resultado[i] == 'S':
                new_local = (local_atual[0] + 1, local_atual[1])
            elif resultado[i] == 'E':
                new_local = (local_atual[0], local_atual[1] + 1)
            elif resultado[i] == 'W':
                new_local = (local_atual[0], local_atual[1] - 1)
            # Verifica se ta fora do mapa
            if new_local[0] < 0 or new_local[0] > dimension_map - 1 or new_local[1] < 0 or new_local[
                1] > dimension_map - 1:
                print('DE CARA NO MURO!!')
                out = True
            # Verifica se morreu
            elif mapa.matrix[new_local[0]][new_local[1]] in ['wumpus', 'pit']:
                print('IH, PASSOU MAL!!!')
                death = True
            # Verifica se escapou
            # elif new_local == (0, 0) and qtd_actions > 5:
            # agent_win = True
        print(f'MOVE: {resultado[i]}')
        mapa.printMatrix(local_atual)
        # Verifica se venceu

        if death:
            print('NÃO CARA, QUE LOUCURA! COMO VOCÊ É BURRO!')
            break

        if new_local == (0, 0) and gold:
            print('GANHOU UM GUARAVITA! PARABÉNS!')
            break

        if not out and not tiro:
            local_atual = new_local

    # self.cromossomo = moves_accepts
    # print(moves_accepts)

    plt.plot(ag.lista_solucoes)
    plt.title("Acompanhamento de pontuações")
    plt.show()
