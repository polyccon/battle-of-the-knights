def update_position(move, state):
    if move['dir'] == 'N' and state[move['player']][0][0] == 0:
        state[move['player']][1] == 'DROWNED'
        state[move['player']][3] == 0
        state[move['player']][4] == 0
    elif move == 'S' and state[move['player']][0][0] == 7:
        state[move['player']][1] == 'DROWNED'
        state[move['player']][3] == 0
        state[move['player']][4] == 0
    elif move == 'E' and state[move['player']][0][1] == 0:
        state[move['player']][1] == 'DROWNED'
        state[move['player']][3] == 0
        state[move['player']][4] == 0
    elif move == 'W' and state[move['player']][0][1] == 7:
        state[move['player']][1] == 'DROWNED'
        state[move['player']][3] == 0
        state[move['player']][4] == 0
    elif move['dir'] == 'N':
        state[move['player']][0] == (state[move['player']][0][0] -1, state[move['player']][0][1])
    elif move['dir'] == 'E':
        state[move['player']][0] == (state[move['player']][0][0], state[move['player']][0][1] + 1)
    elif move['dir'] == 'S':
        state[move['player']][0] == (state[move['player']][0][0] +1, state[move['player']][0][1])
    elif move['dir'] == 'W':
        state[move['player']][0][1] == (state[move['player']][0][0], state[move['player']][0][1]- 1)
    return state
