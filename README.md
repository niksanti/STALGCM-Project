# STALGCM-Project

Run TwoWayFAMain.py in and IDE to open the machine
then upload the two-way-machine-definition-file.txt with the proper format

Format for editing the two-way-machine-definition-file:

seperate them by spaces (' ')

line 1: number of states
line 2: list of states 
line 3: number of inputs
line 4: list of inputs
line 5: number of transitions
line 6*: list of transitions in the format q s q' d ("from State" "input" "To State" "Direction")
after lists of transitions
3rd last line: start state
2nd last line: accept state
last line: reject state