from collections import namedtuple

def update_position(move, state):
    position = state[move['player']][0]
    row = state[move['player']][0][0]
    column = state[move['player']][0][1]

    if move['dir'] == 'N':
        newrow= row -1
        newcolumn = column
    elif move['dir'] == 'E':
        newrow= row
        newcolumn = column -1
    elif move['dir'] == 'S':
        newrow= row +1
        newcolumn = column
    else:
        newrow= row
        newcolumn = column +1

    #checking if move is in range
    if  newrow not in range(0,8) or newcolumn not in range(0,8):
        state[move['player']][1] = 'DROWNED'
        state[move['player']][3] = 0
        state[move['player']][4] = 0

        #if player has items drops them before drowning
        if state[move['player']][2] is not None:
            state[state[move['player']][2]][0] == state[move['player']][0]

        #update player position
        state[move['player']][0] = (newrow, newcolumn)

    return state
