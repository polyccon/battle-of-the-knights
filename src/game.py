import ast

from .weapons import get_weapon
from .position import update_position
from .fight import fight

def open_moves(filename):
    moves = open(moves_file, 'r').read()
    return ast.literal_eval(moves)

def update_state(moves):
    in_state= {
        'red': [(0,0),'LIVE',None,1,1],
        'blue': [(7,0),'LIVE',None,1,1],
        'green': [(7,7),'LIVE',None,1,1],
        'yellow': [(0,7),'LIVE',None,1,1],
        'magic_staff': [(5,2),False],
        'helmet': [(5,5),False],
        'dagger': [(2,5),False],
        'axe': [(2,2),False],
        }

    for move in moves:
        newstate = fight(move, get_weapon(move, update_position(move, in_state)))
    return newstate

def export_state(newstate):
    output_file = 'Result: ' + moves_file
    file = open(output_file, 'w')
    file.write(str(newstate))
    file.close()

#print (update_state('moves.txt', 'result.txt'))
