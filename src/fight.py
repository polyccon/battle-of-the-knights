from .constants import *

def fight(move, state):
    attacker = state[move['player']]
    #check if any of the other 3 knights is on the same tile
    for player in ['red', 'blue', 'green', 'yellow']:
        if player == move['player']:
            continue

        defender = state[player]
        #if yes there is a fight:
        if attacker[ LOCATION ] == defender[ LOCATION ]:
            attacker[ ATTACK ] += defender[ ATTACK ] + 0.5
            defender[ DEFENCE ] += attacker[ DEFENCE ]

            #check which one has more points
            if attacker[ ATTACK ] > defender[ DEFENCE ]:
                state[defender[ WEAPON ]][ OWNED] = False
                defender[ STATUS ] = 'DEAD'
                defender[ ATTACK ] = 0
                defender[ DEFENCE ] = 0
                defender[ WEAPON ] = None

            elif attacker[ ATTACK ] < defender[ DEFENCE ]:
                state[attacker[ WEAPON ]][ OWNED ] = False
                attacker[ STATUS ] = 'DEAD'
                attacker[ ATTACK ] = 0
                attacker[ DEFENCE ] = 0
                attacker[ WEAPON ] = None

            #remove surprise points from final output of state
            attacker[ ATTACK ] -= 0.5
            attacker[ ATTACK ] = int(attacker[3])

    return state
