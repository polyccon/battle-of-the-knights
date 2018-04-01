def fight(move, state):
    attacker = state[move['player']]
    #check if any of the other 3 knights is on the same tile
    for player in ['red', 'blue', 'green', 'yellow']:
        if player == move['player']:
            continue

        defender = state[player]
            #if yes:
            #The attacker takes their base attack score and adds any item modifiers.
            #The attacker adds 0.5 to their attack score (for the element of surprise).
            #The defender takes their base defence score and adds any item modifiers.
        if attacker[0] == defender[0]:
            attacker[3] += defender[3] + 0.5
            defender[4] += attacker[4]
            weapon1 = attacker[2]
            weapon2 = defender[2]
            attacker[2] = weapon2
            defender[2] = weapon1

            #check which one has more points
            if attacker[3] > defender[4]:
                print (state[defender[2]])
                state[defender[2]][1] = False
                print (state[defender[2]])
                defender[1] = 'DEAD'
                defender[3] = 0
                defender[4] = 0
                defender[2] = None

            elif attacker[3] < defender[4]:
                print (state[attacker[2]])
                state[attacker[2]][1] = False
                print (state[attacker[2]])
                attacker[1] = 'DEAD'
                attacker[3] = 0
                attacker[4] = 0
                attacker[2] = None

            #remove surprise points from final output of state
            attacker[3] -= 0.5
            attacker[3] = int(attacker[3])

    return state
