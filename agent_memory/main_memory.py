from agent_memory import Agent
from map import Map
import time
from random import randint


def start() -> int:
    mapa = Map(5, map_fix=True)
    agent = Agent(5)
    qtd_moves = 0
    print(f'Local atual: {agent.actual_coord}')
    perceptions = mapa.matrix_perceptions[agent.actual_coord[0]][agent.actual_coord[1]]
    print(f'Percepções: {perceptions}')
    mapa.printMatrix(agent.actual_coord)
    time.sleep(3)
    removed = False

    while True:
        chance = randint(0, 100)
        if agent.hasGold() and removed is False:
            mapa.removeGold(agent.actual_coord)
            removed = True
        if agent.hasGold() and chance > 25:
            # Acrescentar chance de mover seguindo as casas seguras ou não quando tiver o ouro
            print(f'Chance: {chance}')
            move_to_do = agent.moveWithGold()
        else:
            move_to_do = agent.conditions(agent.actual_coord[0], agent.actual_coord[1], perceptions)
        print(f'Movimento: {move_to_do.name} | Direção: {move_to_do.direction}')
        agent.doMove(move_to_do)
        if move_to_do.name == 'shoot':
            mapa.shootWumpus(move_to_do.direction, agent.actual_coord)
        qtd_moves += 1
        if mapa.scream: print('Wumpus está morto!')
        print(f'Local atual: {agent.actual_coord}')
        perceptions = mapa.matrix_perceptions[agent.actual_coord[0]][agent.actual_coord[1]]
        print(f'Percepções: {perceptions}')
        mapa.printMatrix(agent.actual_coord)
        if agent.actual_coord in mapa.elementsPositions['pit']:
            print('You fell in the pit!')
            break
        if agent.actual_coord in mapa.elementsPositions['wumpus']:
            print('You were devoured by the Wumpus!')
            break
        agent.safe_coords.append(agent.actual_coord)
        time.sleep(1)
        if agent.hasWinner():
            print('Você venceu! yeeeeeeeeeeeeee'.upper())
            break
    return qtd_moves


if __name__ == '__main__':
    qt_moves = start()
    print(f'Quantidade de Movimentos: {qt_moves}')
