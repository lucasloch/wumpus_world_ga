from action import Action
from random import choice


class Agent(object):
    def __init__(self, size_map: int = 4):
        self.size_map = size_map
        self.gold = False
        self.arrow = True
        self.actual_coord = (0, 0)

    def conditions(self, line, column, perceptions: list) -> Action:
        if 'glitter' in perceptions and self.hasGold() is False:
            return Action('pickup', '')

        if line == 0:
            if column == 0:
                if 'scream' in perceptions:
                    return Action('move', direction=choice(['S', 'E']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=choice(['S', 'E']))
                if 'breeze' in perceptions:
                    return Action('move', direction=choice(['S', 'E']))
                return Action('move', choice(['S', 'E']))
            elif column == (self.size_map - 1):
                if 'scream' in perceptions:
                    return Action('move', direction=choice(['S', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=choice(['S', 'W']))
                if 'breeze' in perceptions:
                    return Action('move', direction=choice(['S', 'W']))
                return Action('move', choice(['S', 'W']))
            else:
                if 'scream' in perceptions:
                    return Action('move', direction=choice(['S', 'E', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=choice(['S', 'E', 'W']))
                if 'breeze' in perceptions:
                    return Action('move', direction=choice(['S', 'E', 'W']))
                return Action('move', choice(['S', 'E', 'W']))

        if line == (self.size_map - 1):
            if column == 0:
                if 'scream' in perceptions:
                    return Action('move', direction=choice(['N', 'E']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=choice(['N', 'E']))
                if 'breeze' in perceptions:
                    return Action('move', direction=choice(['N', 'E']))
                return Action('move', choice(['N', 'E']))
            elif column == (self.size_map - 1):
                if 'scream' in perceptions:
                    return Action('move', direction=choice(['N', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=choice(['N', 'W']))
                if 'breeze' in perceptions:
                    return Action('move', direction=choice(['N', 'W']))
                return Action('move', choice(['N', 'W']))
            else:
                if 'scream' in perceptions:
                    return Action('move', direction=choice(['N', 'E', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=choice(['N', 'E', 'W']))
                if 'breeze' in perceptions:
                    return Action('move', direction=choice(['N', 'E', 'W']))
                return Action('move', choice(['N', 'E', 'W']))

        else:
            if column == 0:
                if 'scream' in perceptions:
                    return Action('move', direction=choice(['S', 'N', 'E']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=choice(['S', 'N', 'E']))
                if 'breeze' in perceptions:
                    return Action('move', direction=choice(['S', 'N', 'E']))
                return Action('move', choice(['S', 'N', 'E']))
            elif column == (self.size_map - 1):
                if 'scream' in perceptions:
                    return Action('move', direction=choice(['S', 'N', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=choice(['S', 'N', 'W']))
                if 'breeze' in perceptions:
                    return Action('move', direction=choice(['S', 'N', 'W']))
                return Action('move', choice(['S', 'N', 'W']))
            else:
                if 'scream' in perceptions:
                    return Action('move', direction=choice(['S', 'N', 'E', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=choice(['S', 'N', 'E', 'W']))
                if 'breeze' in perceptions:
                    return Action('move', direction=choice(['S', 'N', 'E', 'W']))
                return Action('move', choice(['S', 'N', 'E', 'W']))

    def doMove(self, action: Action):
        if action.name == 'pickup':
            self.pickUp()
        elif action.name == 'shoot':
            self.shoot()
        else:
            if action.direction == 'N':
                self.actual_coord = self.actual_coord[0] - 1, self.actual_coord[1]
            elif action.direction == 'S':
                self.actual_coord = self.actual_coord[0] + 1, self.actual_coord[1]
            elif action.direction == 'E':
                self.actual_coord = self.actual_coord[0], self.actual_coord[1] + 1
            elif action.direction == 'W':
                self.actual_coord = self.actual_coord[0], self.actual_coord[1] - 1
        
    def shoot(self):
        self.arrow = False

    def pickUp(self):
        self.gold = True

    def hasGold(self):
        return self.gold

    def hasWinner(self) -> bool:
        if self.actual_coord == (0, 0) and self.hasGold():
            return True
        else:
            return False
