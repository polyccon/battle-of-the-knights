from .constants import *

def get_position(move, state):
    row = state[move['player']][ LOCATION ][0]
    column = state[move['player']][ LOCATION ][1]

    if move['dir'] == 'N':
        newrow= row -1
        newcolumn = column
    elif move['dir'] == 'E':
        newrow= row
        newcolumn = column +1
    elif move['dir'] == 'S':
        newrow= row +1
        newcolumn = column
    else:
        newrow= row
        newcolumn = column -1
    return (newrow, newcolumn)

def update_position(move, state):
    new_position = get_position(move,state)

    #checking if move is in range
    if  new_position[0] not in range(0,8) or new_position[1] not in range(0,8):
        state[move['player']][ STATUS ] = 'DROWNED'
        state[move['player']][ ATTACK ] = 0
        state[move['player']][ DEFENCE ] = 0

        #if player has items drops them before drowning
        if state[move['player']][2] is not None:
            state[state[move['player']][2]][ LOCATION ] == state[move['player']][ LOCATION ]

        #update player position
    state[move['player']][ LOCATION ] = new_position

    #update position of weapon if owned by a knight
    if state[move['player']][ WEAPON ] is not None:
        state[state[move['player']][2]][ LOCATION ] = new_position
    return state
