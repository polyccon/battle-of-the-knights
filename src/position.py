def get_position(move, state):
    row = state[move['player']][0][0]
    column = state[move['player']][0][1]

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
        state[move['player']][1] = 'DROWNED'
        state[move['player']][3] = 0
        state[move['player']][4] = 0

        #if player has items drops them before drowning
        if state[move['player']][2] is not None:
            state[state[move['player']][2]][0] == state[move['player']][0]

        #update player position
    state[move['player']][0] = new_position

    #update position of weapon if owned by a knight
    if state[move['player']][2] is not None:
        state[state[move['player']][2]][0] = new_position
    return state
