from agent import Agent
from map import Map
from time import sleep


def start() -> int:
    dimension_map = 4
    mapa = Map(dimension_map, 3, 1, 1)
    agent = Agent(dimension_map)
    qtd_moves = 0
    print(f'Local atual: {agent.actual_coord}')
    perceptions = mapa.matrix_perceptions[agent.actual_coord[0]][agent.actual_coord[1]]
    print(f'Percepções: {perceptions}')
    mapa.printMatrix(agent.actual_coord)
    sleep(3)

    while True:
        move_to_do = agent.conditions(agent.actual_coord[0], agent.actual_coord[1], perceptions)
        print(f'Movimento: {move_to_do.name} | Direção: {move_to_do.direction}')
        agent.doMove(move_to_do)
        if move_to_do.name == 'pickup':
            mapa.removeGold(agent.actual_coord)
        if move_to_do.name == 'shoot':
            mapa.shootWumpus(move_to_do.direction, agent.actual_coord)
        qtd_moves += 1
        if mapa.scream:
            print('Você ouve um grito')
            mapa.scream = False
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
        sleep(1)
        if agent.hasWinner():
            print('Você venceu! yeeeeeeeeeeeeee'.upper())
            break
    return qtd_moves


if __name__ == '__main__':
    qt_moves = start()
    print(f'Quantidade de Movimentos: {qt_moves}')
