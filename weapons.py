def get_weapon(move,state):
    for weapon in ['magic_staff', 'helmet', 'dagger', 'axe']:
        if state[weapon][0] == state[move['player']][0] and state[move['player']][2] is None:
            state[weapon][0] = state[move['player']][0]
            state[weapon][0] = True
            state[move['player']][2] = weapon
            if weapon == 'axe':
                state[move['player']][2] = 3
            elif weapon == 'dagger':
                state[move['player']][2] = 2
            elif weapon == 'magic_staff':
                state[move['player']][2] = 2
                state[move['player']][3] = 2
            elif weapon == 'helmet':
                state[move['player']][3] = 2
    return state
