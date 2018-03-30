def get_axe(move, state):
    return any([all([move['dir'] == 'N', state[move['player']][2] is None, state[move['player']][0] == (3,2)]),
all([move['dir'] == 'S', state[move['player']][2] is None, state[move['player']][0] == (1,2)]),
all([move['dir'] == 'E', state[move['player']][2] is None, state[move['player']][0] == (2,1)]),
all([move['dir'] == 'W', state[move['player']][2] is None, state[move['player']][0] == (2,3)])])

def get_dagger(move, state):
    return any([all([move['dir'] == 'N', state[move['player']][2] is None, state[move['player']][0] == (3,5)]),
all([move['dir'] == 'S', state[move['player']][2] is None, state[move['player']][0] == (1,5)]),
all([move['dir'] == 'E', state[move['player']][2] is None, state[move['player']][0] == (2,6)]),
all([move['dir'] == 'W', state[move['player']][2] is None, state[move['player']][0] == (2,4)])])

def get_helmet(move, state):
    return any([all([move['dir'] == 'N', state[move['player']][2] is None, state[move['player']][0] == (6,5)]),
all([move['dir'] == 'S', state[move['player']][2] is None, state[move['player']][0] == (4,5)]),
all([move['dir'] == 'E', state[move['player']][2] is None, state[move['player']][0] == (5,4)]),
all([move['dir'] == 'W', state[move['player']][2] is None, state[move['player']][0] == (5,6)])])

def get_magic(move, state):
    return any([all([move['dir'] == 'N', state[move['player']][2] is None, state[move['player']][0] == (6,2)]),
all([move['dir'] == 'S', state[move['player']][2] is None, state[move['player']][0] == (4,2)]),
all([move['dir'] == 'E', state[move['player']][2] is None, state[move['player']][0] == (5,1)]),
all([move['dir'] == 'W', state[move['player']][2] is None, state[move['player']][0] == (5,3)])])

def get_weapon(move, state):
    if get_axe(move, state):
        state[move['player']][0] == (2,2)
        state[move['player']][2] == 3
        state['axe'] == [state[move['player']][0], True ]
    elif get_dagger(move, state):
        state[move['player']][0] == (2,5)
        state[move['player']][2] == 2
        state['dagger'] == [state[move['player']][0], True ]
    elif get_magic(move, state):
        state[move['player']][0] == (6,2)
        state[move['player']][2] == 2
        state[move['player']][3] == 2
        state['magic'] == [state[move['player']][0], True ]
    elif get_helmet(move, state):
        state[move['player']][0] == (5,5)
        state[move['player']][3] == 2
        state['helmet'] == [state[move['player']][0], True ]
    return state
