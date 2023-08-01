import tkinter as tk

window = tk.TK()

window.title("Two-Way Accepter")



class TwoWayAccepter:
    def __init__(self, alphabet, transitions, start_state, accept_state, reject_state):
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state

    def run(self, input_string):
        tape = list(input_string)
        head = 0
        current_state = self.start_state

        while current_state != self.accept_state and current_state != self.reject_state:
            current_symbol = tape[head]

            if current_symbol not in self.input_alphabet:
                current_state = self.reject_state
                break

            if (current_state, current_symbol) not in self.transitions:
                current_state = self.reject_state
                break

            new_state, move_direction = self.transitions[(current_state, current_symbol)]
            if move_direction == 'R':
                head += 1
            elif move_direction == 'L':
                head = max(head - 1, 0)

            current_state = new_state

        return current_state == self.accept_state

# Example usage:
f = open("test.txt", 'r')
lines = []
lines = f.readlines()
f.close()

total_lines = len(lines)

if total_lines < 8:
    print("invalid machine definition file")
else:
    number_of_states = int(lines[0])
    states = lines[1].split()
    number_of_inputs = int(lines[2])
    inputs = lines[3].split()
    number_of_transitions = int(lines[4])
    transition = {}
    for i in range(5, total_lines-3):
        fields = lines.split(' ')
        state = fields[0]
        symbol = fields[1]
        new_state = fields[2]
        direction = fields[3]
        move = set(state, symbol)
        move2 = set(new_state, direction)
        transition[move] = move2
    start = lines[total_lines - 3]
    accept = lines[total_lines - 2]
    reject = lines[total_lines - 1]

if __name__ == "__main__":
    # Define the alphabet
    alphabet = set(inputs)

    # Define the transitions (current_state, input_symbol) -> (next_state, direction)
    transitions = transition

    # Define the start state and accept states
    start_state = start
    accept_state = accept
    reject_state = reject

    # Create the two-way accepter
    accepter = TwoWayAccepter(alphabet, transitions, start_state, accept_state, reject_state)

    # Test the recognition
    input_string = "1100"
    if accepter.run(input_string):
        print(f"{input_string} is accepted.")
    else:
        print(f"{input_string} is rejected.")

    # Test the generation
    generated_string = accepter.generate(max_length=10)
    print(f"Generated string: {generated_string}")


window.mainloop()