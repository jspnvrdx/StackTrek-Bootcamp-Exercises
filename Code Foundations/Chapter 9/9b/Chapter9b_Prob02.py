import os
os.system('cls||clear')

#----CODE STARTS HERE------

def count_reactions(reactions): 
    reactions_tally = dict()
    for react in reactions:
        react = react.lower()
        if react not in reactions_tally:
            reactions_tally[react] = 1
        else:
            reactions_tally[react] = reactions_tally.get(react, 0) + 1
    return reactions_tally

print(count_reactions(reactions = ["angry", "Care", "like", "like"]))