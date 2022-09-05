from action import Action
import random


class Agent(object):
    def __init__(self, size_map: int = 4):
        self.size_map = size_map
        self.gold = False
        self.arrow = True
        self.actual_coord = (0, 0)
        self.safe_coords = [(0, 0)]

    def conditions(self, line, column, perceptions: list) -> Action:
        if 'glitter' in perceptions: return Action('pickup', '')

        if line == 0:
            if column == 0:
                if 'scream' in perceptions: return Action('move', direction=random.choice(['S', 'E']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=random.choice(['S', 'E']))
                if 'breeze' in perceptions: return Action('move', direction=random.choice(['S', 'E']))
                return Action('move', random.choice(['S', 'E']))
            elif column == (self.size_map - 1):
                if 'scream' in perceptions: return Action('move', direction=random.choice(['S', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=random.choice(['S', 'W']))
                if 'breeze' in perceptions: return Action('move', direction=random.choice(['S', 'W']))
                return Action('move', random.choice(['S', 'W']))
            else:
                if 'scream' in perceptions: return Action('move', direction=random.choice(['S', 'E', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=random.choice(['S', 'E', 'W']))
                if 'breeze' in perceptions: return Action('move', direction=random.choice(['S', 'E', 'W']))
                return Action('move', random.choice(['S', 'E', 'W']))

        if line == (self.size_map - 1):
            if column == 0:
                if 'scream' in perceptions: return Action('move', direction=random.choice(['N', 'E']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=random.choice(['N', 'E']))
                if 'breeze' in perceptions: return Action('move', direction=random.choice(['N', 'E']))
                return Action('move', random.choice(['N', 'E']))
            elif column == (self.size_map - 1):
                if 'scream' in perceptions: return Action('move', direction=random.choice(['N', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=random.choice(['N', 'W']))
                if 'breeze' in perceptions: return Action('move', direction=random.choice(['N', 'W']))
                return Action('move', random.choice(['N', 'W']))
            else:
                if 'scream' in perceptions: return Action('move', direction=random.choice(['N', 'E', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=random.choice(['N', 'E', 'W']))
                if 'breeze' in perceptions: return Action('move', direction=random.choice(['N', 'E', 'W']))
                return Action('move', random.choice(['N', 'E', 'W']))

        else:
            if column == 0:
                if 'scream' in perceptions: return Action('move', direction=random.choice(['S', 'N', 'E']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=random.choice(['S', 'N', 'E']))
                if 'breeze' in perceptions: return Action('move', direction=random.choice(['S', 'N', 'E']))
                return Action('move', random.choice(['S', 'N', 'E']))
            elif column == (self.size_map - 1):
                if 'scream' in perceptions: return Action('move', direction=random.choice(['S', 'N', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=random.choice(['S', 'N', 'W']))
                if 'breeze' in perceptions: return Action('move', direction=random.choice(['S', 'N', 'W']))
                return Action('move', random.choice(['S', 'N', 'W']))
            else:
                if 'scream' in perceptions: return Action('move', direction=random.choice(['S', 'N', 'E', 'W']))
                if 'stench' in perceptions:
                    action = 'move' if not self.arrow else 'shoot'
                    return Action(action, direction=random.choice(['S', 'N', 'E', 'W']))
                if 'breeze' in perceptions: return Action('move', direction=random.choice(['S', 'N', 'E', 'W']))
                return Action('move', random.choice(['S', 'N', 'E', 'W']))

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

    def moveWithGold(self):
        if (self.actual_coord[0] - 1, self.actual_coord[1]) in self.safe_coords:
            return Action('move', 'N')
        elif (self.actual_coord[0], self.actual_coord[1] - 1) in self.safe_coords:
            return Action('move', 'W')
        elif (self.actual_coord[0] + 1, self.actual_coord[1]) in self.safe_coords:
            return Action('move', 'S')
        elif (self.actual_coord[0], self.actual_coord[1] + 1) in self.safe_coords:
            return Action('move', 'E')

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
