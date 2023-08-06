# Model 

class MachineModel:
    # Constructor
    def __init__(self):

        self._total_lines = 0
        self._number_of_states = 0
        self._number_of_alphabets = 0
        self._number_of_transitions = 0
        self._states = []
        self._alphabets = []
        self._transitions = {}
        self._initial_state = ""
        self._final_state_accept = ""
        self._final_state_reject = ""
        self._input_string = ""
        self._current_input_list = []
        self._transition_info_list = []
        self._generated_string = ""
        self._accepter_status = False

    # Method for handling the file upload
    def handle_file_upload(self, path_file_directory):
        # Read the file
        f = open(path_file_directory, "r")
        lines = []
        lines = f.readlines()
        f.close()

        total_lines = len(lines)

        if total_lines < 8:
            print("Invalid machine definition file.")
        else:
            number_of_states = int(lines[0])
            states = lines[1].split()
            self.set_states(states)

            number_of_alphabets = int(lines[2])
            alphabets = lines[3].split()
            self.set_alphabets(alphabets)

            number_of_transitions = int(lines[4])
            transitions = {}
            for i in range(5, total_lines - 4):
                fields = lines[i].split(' ')
                state = fields[0]
                alphabet = fields[1]
                new_state = fields[2]
                # Remove the '\n' character
                direction = fields[3][0]
                move = (state, alphabet)
                move2 = (new_state, direction)
                transitions[move] = move2
            self.set_transitions(transitions)
            
            # Remove the '\n' character
            start = lines[total_lines - 4][:-1]
            self.set_initial_state(start)

            # Remove the '\n' character
            accept = lines[total_lines - 3][:-1]
            self.set_final_state_accept(accept)

            # Remove the '\n' character
            reject = lines[total_lines - 2]
            self.set_final_state_reject(reject)
            # pass

            # Remove the '\n' character
            input_string = lines[total_lines - 1]
            self.set_input_string(input_string)

            # Check the console
            print(f"States: {self.get_states()}")
            print(f"Alphabets: {self.get_alphabets()}")

            # Reformat the printing of the transitions
            print(f"Transitions: ")
            for transition in self.get_transitions():
                print(f"{transition} -> {self.get_transitions()[transition]}")

            print(f"Start state: {self.get_initial_state()}")
            print(f"Accepting state: {self.get_final_state_accept()}")
            print(f"Rejecting state: {self.get_final_state_reject()}")
            print(f"Input string: {self.get_input_string()}")

            print("\nRunning the machine...")
            # Call the method for running the machine
            TwoWayAccepterMachine = self.run_TwoWayAccepter(self.get_input_string())

            # Check the console to test recognition
            if TwoWayAccepterMachine == True:
                print(f"\nOutput: ")
                print(f"{input_string} is accepted.")
                self.set_accepter_status(True)
            else:
                print(f"\nOutput: ")
                print(f"{input_string} is rejected.")
                self.set_accepter_status(False)

            # Call the method for generating the string
            generated_string = self.generate()
            self.set_generated_string(generated_string)
            print(f"Generated string: {self.get_generated_string()}")


    # Method for running the machine: Two Way Accepter
    def run_TwoWayAccepter(self, input_string):
        tape = list(input_string)
        head = 0
        current_state = self.get_initial_state()
        accept_state = self.get_final_state_accept()
        reject_state = self.get_final_state_reject()
        transition_info_string = ""
        current_input_list = []
        transition_info_list = []
        
        while current_state != accept_state and current_state != reject_state:
            current_input = tape[head]
            current_input_list.append(current_input)

            if current_input not in self.get_alphabets():
                current_state = reject_state
                break

            if (current_state, current_input) not in self.get_transitions():
                current_state = reject_state
                break
            
            new_state, move_direction = self.get_transitions()[(current_state, current_input)]

            transition_info_string = f"({current_state}, {current_input}) -> ({new_state}, {move_direction})\n"
            transition_info_list.append(transition_info_string)

            if move_direction == "R":
                head += 1
            elif move_direction == "L":
                head = max(head - 1, 0)

            current_state = new_state


        self.set_current_input_list(current_input_list)
        self.set_transition_info_list(transition_info_list)

        
        # Print all the symbols and its transition info in the console
        tempInputList = []
        tempTransitionInfoList = []

        tempInputList = self.get_current_input_list()
        tempTransitionInfoList = self.get_transition_info_list()

        for i in range(len(tape)):
            print(f"Step {i}: ", end=" ")
            print(f"Current input: {tempInputList[i]}", end=" ")
            print(f"\tTransition info: {tempTransitionInfoList[i]}", end=" ")

        

        return current_state == self.get_final_state_accept()
    

    def generate(self, max_length=100):
        tape = [' '] * max_length
        head = 0
        current_state = self.get_initial_state()
        accept_state = self.get_final_state_accept()
        reject_state = self.get_final_state_reject()

        while current_state != accept_state and current_state != reject_state:
            if (current_state, ' ') not in self.get_transitions():
                current_state = reject_state
                break

            new_state, move_direction = self.get_transitions()[(current_state, ' ')]
            if move_direction == 'R':
                head += 1
            elif move_direction == 'L':
                head = max(head - 1, 0)

            current_state = new_state

        if current_state == reject_state:
            return None

        while current_state != accept_state:
            if (current_state, ' ') not in self.get_transitions():
                current_state = reject_state
                break

            new_state, move_direction = self.get_transitions()[(current_state, ' ')]
            if move_direction == 'R':
                head += 1
            elif move_direction == 'L':
                head = max(head - 1, 0)

            current_state = new_state

        return ''.join(tape)
    
    # Getters
    
    def get_states(self):
        return self._states

    def get_alphabets(self):
        return self._alphabets
    
    def get_transitions(self):
        return self._transitions
    
    def get_initial_state(self):
        return self._initial_state
    
    def get_final_state_accept(self):
        return self._final_state_accept

    def get_final_state_reject(self):
        return self._final_state_reject

    def get_input_string(self):
        return self._input_string
    
    def get_current_input_list(self):
        return self._current_input_list
    
    def get_transition_info_list(self):
        return self._transition_info_list
    
    def get_generated_string(self):
        return self._generated_string
    
    def get_accepter_status(self):
        return self._accepter_status
    
    
    # Setters

    def set_states(self, states):
        self._states = states

    def set_alphabets(self, alphabets):
        self._alphabets = alphabets

    def set_transitions(self, transitions):
        self._transitions = transitions

    def set_initial_state(self, initial_state):
        self._initial_state = initial_state

    def set_final_state_accept(self, final_state_accept):
        self._final_state_accept= final_state_accept

    def set_final_state_reject(self, final_state_reject):
        self._final_state_reject = final_state_reject

    def set_input_string(self, input_string):
        self._input_string = input_string

    def set_current_input_list(self, current_input_list):
        self._current_input_list = current_input_list

    def set_transition_info_list(self, transition_info_list):
        self._transition_info_list = transition_info_list

    def set_generated_string(self, generated_string):
        self._generated_string = generated_string

    def set_accepter_status(self, accepter_status):
        self._accepter_status = accepter_status