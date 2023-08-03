# STALGCM-Project

Format for editing the two-way machine definition file:

seperate them by spaces (' ')

line 1: number of states
line 2: list of states 
line 3: number of inputs
line 4: list of inputs
line 5: number of transitions
line 6*: list of transitions in the format q s q' d ("from State" "input" "To State" "Direction")
after lists of transitions
line 7: start state
line 8: accept state
line 9: reject state