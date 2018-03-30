from weapons import get_weapon
from position import update_position
from fight import fight

moves_1 = [{'player': 'red', 'dir': 'S'}, {'player': 'red', 'dir': 'S'},
        {'player':'blue', 'dir': 'E'}, {'player': 'green', 'dir': 'N'},
        {'player': 'yellow', 'dir':'N'}]

in_state= {
    'red': [(0,0),'LIVE',None,1,1],
    'blue': [(7,0),'LIVE',None,1,1],
    'green': [(7,7),'LIVE',None,1,1],
    'yellow': [(0,7),'LIVE',None,1,1],
    'magic_staff': [(2,2),False],
    'helmet': [(5,2),False],
    'dagger': [(5,5),False],
    'axe': [(2,5),False],
}

def update_state(moves, state):
    for move in moves:
        newstate = get_weapon(move, fight(move, update_position(move, state)))
    return newstate

print (update_state(moves_1, in_state))
