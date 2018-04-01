from random import randint

from .position import update_position

def findsame(object, val):
  return {k:v for k, v in object.items() if v[0] == val}

def is_weapon(move, state):
    weapons = {'magic_staff': state['magic_staff'],
                'helmet': state['helmet'],
                'dagger': state['dagger'],
                'axe': state['axe']}

    player_pos = state[move['player']][0]
    weapons_in_tile = findsame(weapons, player_pos)

    if len(weapons_in_tile.keys()) >1:
        rand_ind = randint(0, len(list(weapons_in_tile.keys()))-1)
        weapon = list(weapons_in_tile.keys())[rand_ind]
    elif len(weapons_in_tile.keys()) == 1:
        weapon = list(weapons_in_tile.keys())[0]
    else:
        weapon = None
    return weapon


def get_weapon(move, state):
    if is_weapon(move,state) is not None and state[move['player']][2] is None:
        weapon = is_weapon(move, state)
        state[weapon][0] = state[move['player']][0]
        state[weapon][1] = True
        state[move['player']][2] = weapon
        if weapon == 'axe':
            state[move['player']][2] = 'axe'
            state[move['player']][3] = 3
        elif weapon == 'dagger':
            state[move['player']][2] = 'dagger'
            state[move['player']][3] = 2
        elif weapon == 'magic_staff':
            state[move['player']][2] = 'magic_staff'
            state[move['player']][3] = 2
            state[move['player']][4] = 2
        elif weapon == 'helmet':
            state[move['player']][2] = 'helmet'
            state[move['player']][4] = 2
    return state
