import tkinter as tk

window = tk.TK()

class TwoWayAccepter:
    def __init__(self, alphabet, transitions, start_state, accept_states):
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def recognize(self, input_string):
        current_state = self.start_state
        index = 0

        while index < len(input_string):
            char = input_string[index]
            if char not in self.alphabet:
                return False

            if (current_state, char) in self.transitions:
                current_state, direction = self.transitions[(current_state, char)]
                if direction == 'L':
                    index -= 1
                elif direction == 'R':
                    index += 1
            else:
                return False

        return current_state in self.accept_states

    def generate(self, max_length):
        current_state = self.start_state
        output_string = ""

        while len(output_string) < max_length:
            possible_transitions = [
                (char, state, direction)
                for ((state, char), (next_state, direction)) in self.transitions.items()
                if state == current_state
            ]

            if not possible_transitions:
                break

            selected_transition = possible_transitions[0]
            char, next_state, direction = selected_transition
            output_string += char

            if direction == 'L':
                current_state = next_state
            elif direction == 'R':
                current_state = next_state
                output_string = char + output_string

        return output_string

# Example usage:
if __name__ == "__main__":
    # Define the alphabet
    alphabet = {'0', '1'}

    # Define the transitions (current_state, input_symbol) -> (next_state, direction)
    transitions = {
        ('q0', '0'): ('q0', 'R'),
        ('q0', '1'): ('q0', 'R'),
        ('q0', ' '): ('q1', 'L'),
        ('q1', '0'): ('q1', 'L'),
        ('q1', '1'): ('q1', 'L'),
        ('q1', ' '): ('q2', 'R'),
    }

    # Define the start state and accept states
    start_state = 'q0'
    accept_states = {'q2'}

    # Create the two-way accepter
    accepter = TwoWayAccepter(alphabet, transitions, start_state, accept_states)

    # Test the recognition
    input_string = "1100"
    if accepter.recognize(input_string):
        print(f"{input_string} is in the language.")
    else:
        print(f"{input_string} is not in the language.")

    # Test the generation
    generated_string = accepter.generate(max_length=10)
    print(f"Generated string: {generated_string}")


window.mainloop()