class Action(object):
    def __init__(self, name: str, direction: str):
        self.name = name
        self.direction = direction

    def __repr__(self) -> str:
        return f'{str(self.name)}: {str(self.direction)}'


table_of_actions = {
    'N': Action('move', 'N'),
    'S': Action('move', 'S'),
    'E': Action('move', 'E'),
    'W': Action('move', 'W'),
    'P': Action('pickup', ''),
    'Z': Action('shoot', 'N'),
    'X': Action('shoot', 'S'),
    'C': Action('shoot', 'E'),
    'V': Action('shoot', 'W')
}
''',
    'P': Action('pickup', ''),
    'Z': Action('shoot', 'N'),
    'X': Action('shoot', 'S'),
    'C': Action('shoot', 'E'),
    'V': Action('shoot', 'W')
'''
