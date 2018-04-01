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

def update_weapon(player, weapon):
    if weapon == 'axe':
        player[2] = 'axe'
    elif weapon == 'dagger':
        player[2] = 'dagger'
    elif weapon == 'magic_staff':
        player[2] = 'magic_staff'
    elif weapon == 'helmet':
        player[2] = 'helmet'
    return player

def update_weapon_points(player, weapon):
    if weapon == 'axe':
        player[3] = 3
    elif weapon == 'dagger':
        player[3] = 2
    elif weapon == 'magic_staff':
        player[3] = 2
        player[4] = 2
    elif weapon == 'helmet':
        player[4] = 2
    return player

def get_weapon(move, state):
    player = state[move['player']]
    if is_weapon(move,state) is not None and player[2] is None:
        weapon = is_weapon(move, state)
        state[weapon][0] = state[move['player']][0]
        state[weapon][1] = True
        player[2] = weapon
        update_weapon(player, weapon)
        update_weapon_points(player, weapon)
    return state
