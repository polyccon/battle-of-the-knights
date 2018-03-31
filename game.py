import ast

from weapons import get_weapon
from position import update_position
from fight import fight

def update_state(moves_file, output_file ):
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
    moves = open(moves_file, 'r').read()
    moves = ast.literal_eval(moves)

    for move in moves:
        newstate = fight(move, get_weapon(move, update_position(move, in_state)))

    file = open(output_file, 'w')
    file.write(str(newstate))
    file.close()
    return newstate

#print (update_state('moves.txt', 'result.txt'))
