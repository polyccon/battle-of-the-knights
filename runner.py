import sys
from src.game import update_state, open_moves, export_state


result = update_state(open_moves(sys.argv[1]))
print (result)

if sys.argv[2] == 'yes':
    export_state(result)
