def fight(move, state):
    for defender in ['red', 'blue', 'green', 'yellow']:
        if defender == move['player']:
            continue
        if state[move['player']][0] == state[defender][0]:
            state[move['player']][3] += state[defender][3] + 0.5
            state[defender][4] += state[move['player']][4]
            if state[move['player']][3] > state[defender][4]:
                state[defender][1] == 'DEAD'
            elif state[move['player']][3] < state[defender][4]:
                state[move['player']][1] == 'DEAD'
    return state
