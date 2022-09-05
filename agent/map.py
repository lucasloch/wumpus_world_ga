from random import randrange


class Map(object):
    def __init__(self, dimension: int = 4, n_pits: int = 3, n_wumpus: int = 1, n_golds: int = 1, map_fix=False):
        self.dimension = dimension
        self.n_pits = n_pits
        self.n_wumpus = n_wumpus
        self.n_golds = n_golds
        self.avalQtdElements()
        self.scream = False
        self.perceptions = {
            "pit": "breeze",
            "gold": "glitter",
            "wumpus": "stench"
        }
        self.elementsPositions = {
            "pit": [],
            "gold": [],
            "wumpus": []
        }
        self.matrix = None
        self.matrix_perceptions = None
        if map_fix:
            if dimension == 4:
                self.createFixMap4()
            elif dimension == 5:
                self.createFixMap5()
            else:
                self.createMap()
        else:
            self.createMap()

    def createFixMap5(self):
        self.dimension = 5
        self.n_pits = 5
        self.n_wumpus = 2
        self.n_golds = 2
        self.scream = False
        self.perceptions = {
            "pit": "breeze",
            "gold": "glitter",
            "wumpus": "stench"
        }
        self.elementsPositions = {
            "pit": [(0, 2), (0, 3), (1, 3), (4, 0), (4, 3)],
            "gold": [(3, 0), (3, 4)],
            "wumpus": [(2, 0), (2, 2)]
        }
        self.matrix = [['empty' for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.matrix_perceptions = [[[] for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.matrix[0][0] = 'agent'
        for x, y in self.elementsPositions['pit']:
            self.matrix[x][y] = 'pit'
            self.addPerceptions(x, y, 'breeze')
        for x, y in self.elementsPositions['gold']:
            self.matrix[x][y] = 'gold'
            self.matrix_perceptions[x][y].append('glitter')
        for x, y in self.elementsPositions['wumpus']:
            self.matrix[x][y] = 'wumpus'
            self.addPerceptions(x, y, 'stench')

    def createFixMap4(self):
        self.dimension = 4
        self.n_pits = 10
        self.n_wumpus = 1
        self.n_golds = 1
        self.scream = False
        self.perceptions = {
            "pit": "breeze",
            "gold": "glitter",
            "wumpus": "stench"
        }
        self.elementsPositions = {
            "pit": [(1, 0), (2, 0), (3, 0), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (3, 2), (3, 3)],
            "gold": [(2, 2)],
            "wumpus": [(3, 1)]
        }
        self.matrix = [['empty' for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.matrix_perceptions = [[[] for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.matrix[0][0] = 'agent'
        for x, y in self.elementsPositions['pit']:
            self.matrix[x][y] = 'pit'
            self.addPerceptions(x, y, 'breeze')
        for x, y in self.elementsPositions['gold']:
            self.matrix[x][y] = 'gold'
            self.matrix_perceptions[x][y].append('glitter')
        for x, y in self.elementsPositions['wumpus']:
            self.matrix[x][y] = 'wumpus'
            self.addPerceptions(x, y, 'stench')

    def avalQtdElements(self) -> None:
        blocks_occupds = self.n_pits + self.n_wumpus + self.n_golds
        blocks_map = self.dimension**2 - int((self.dimension**2)/3)
        if blocks_occupds >= blocks_map:
            self.n_pits = self.dimension - 1
            self.n_wumpus = 1
            self.n_golds = 1

    def createMap(self) -> None:
        # if self.dimension == 0 | self.n_pits == 0 | self.n_golds == 0 | self.n_wumpus == 0:

        self.matrix = [['empty' for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.matrix_perceptions = [[[] for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.matrix[0][0] = 'agent'

        # add gold
        cont = 0
        while True:
            line, column = self.randomPositions()
            self.matrix[line][column] = 'gold'
            self.elementsPositions['gold'].append((line, column))
            self.matrix_perceptions[line][column].append('glitter')
            cont += 1
            if cont == self.n_golds:
                break

        # add wumpus
        cont = 0
        while True:
            line, column = self.randomPositions()
            self.matrix[line][column] = 'wumpus'
            self.elementsPositions['wumpus'].append((line, column))
            self.addPerceptions(line, column, 'stench')
            cont += 1
            if cont == self.n_wumpus:
                break

        # add pits
        cont = 0
        while True:
            line, column = self.randomPositions()
            self.matrix[line][column] = 'pit'
            self.elementsPositions['pit'].append((line, column))
            self.addPerceptions(line, column, 'breeze')
            cont += 1
            if cont == self.n_pits:
                break

    def addPerceptions(self, line: int, column: int, item: str) -> None:
        if item == 'stench':
            self.matrix_perceptions[line][column].append(item)

        if line == 0:
            self.matrix_perceptions[line + 1][column].append(item)
            if column == 0:
                self.matrix_perceptions[line][column + 1].append(item)
            elif column == (len(self.matrix) - 1):
                self.matrix_perceptions[line][column - 1].append(item)
            else:
                self.matrix_perceptions[line][column + 1].append(item)
                self.matrix_perceptions[line][column - 1].append(item)

        elif line == (len(self.matrix) - 1):
            self.matrix_perceptions[line - 1][column].append(item)
            if column == 0:
                self.matrix_perceptions[line][column + 1].append(item)
            elif column == (len(self.matrix) - 1):
                self.matrix_perceptions[line][column - 1].append(item)
            else:
                self.matrix_perceptions[line][column + 1].append(item)
                self.matrix_perceptions[line][column - 1].append(item)

        else:
            self.matrix_perceptions[line + 1][column].append(item)
            self.matrix_perceptions[line - 1][column].append(item)
            if column == 0:
                self.matrix_perceptions[line][column + 1].append(item)
            elif column == (len(self.matrix) - 1):
                self.matrix_perceptions[line][column - 1].append(item)
            else:
                self.matrix_perceptions[line][column + 1].append(item)
                self.matrix_perceptions[line][column - 1].append(item)

    def randomPositions(self) -> tuple:
        x, y = (0, 0)
        while ((x, y) == (0, 0)) or (self.matrix[x][y] != 'empty'):
            x, y = randrange(self.dimension), randrange(self.dimension)
        return x, y

    def shootWumpus(self, direction: str, shoot_direction: tuple) -> bool:
        x, y = shoot_direction
        if direction == 'N':
            x -= 1
        if direction == 'S':
            x += 1
        if direction == 'E':
            y += 1
        if direction == 'W':
            y -= 1
        tuple_local = (x, y)

        if tuple_local in self.elementsPositions['wumpus']:
            self.scream = True
            self.matrix[tuple_local[0]][tuple_local[1]] = 'empty'
            self.elementsPositions['wumpus'].remove((x, y))
            if len(self.elementsPositions['wumpus']) == 0:
                self.elementsPositions['wumpus'].clear()
            return True
        return False

    def killWumpus(self, tuple_local: tuple):
        x, y = tuple_local
        if tuple_local in self.elementsPositions['wumpus']:
            self.matrix[tuple_local[0]][tuple_local[1]] = 'empty'
            self.elementsPositions['wumpus'].remove((x, y))
            if len(self.elementsPositions['wumpus']) == 0:
                self.elementsPositions['wumpus'].clear()
            return True
        return False

    def removeGold(self, coordinate: tuple) -> None:
        self.matrix[coordinate[0]][coordinate[1]] = 'empty'
        self.matrix_perceptions[coordinate[0]][coordinate[1]].remove('glitter')
        if len(self.elementsPositions['gold']) == 0:
            self.elementsPositions['gold'].clear()

    def printMatrix(self, coordinate: tuple) -> None:
        output = ''
        # for line in range(self.dimension - 1, -1, -1): # to invert lines
        for line in range(self.dimension):
            for column in range(self.dimension):
                if coordinate == (line, column):
                    output += '|A'
                else:
                    if self.matrix[line][column] == 'wumpus':
                        output += '|W'
                    elif self.matrix[line][column] == 'gold':
                        output += '|G'
                    elif self.matrix[line][column] == 'pit':
                        output += '|P'
                    else:
                        output += '| '
            output += '|\n'
        print(output)


if __name__ == "__main__":
    mapa = Map(4, map_fix=True)
    mapa.printMatrix((0, 0))
    # print(mapa.matrix_perceptions)
    # mapa.printMatrix((0, 0))

    coord = (2, 2)
    percep = mapa.matrix_perceptions[coord[0]][coord[1]]
    print(percep)
    mapa.matrix_perceptions[coord[0]][coord[1]].remove('glitter')
    percep = mapa.matrix_perceptions[coord[0]][coord[1]]
    print(percep)
