moves = [{'player': 'red', 'dir': 'S'}, {'player': 'red', 'dir': 'S'},
        {'player':'blue', 'dir': 'E'}, {'player': 'green', 'dir': 'N'}]

state= {
    'red': [(0,0),'LIVE',None,1,1],
    'blue': [(7,0),'LIVE',None,1,1],
    'green': [(7,7),'LIVE',None,1,1],
    'yellow': [(0,7),'LIVE',None,1,1],
    'magic_staff': [(2,2),False],
    'helmet': [(5,2),False],
    'dagger': [(5,5),False],
    'axe': [(2,5),False],
}


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
                state[move['player']] == 'DEAD'
    return state
