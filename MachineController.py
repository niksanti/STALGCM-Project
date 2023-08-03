# Controller for the machine

from MachineModel import MachineModel
from MachineView import MachineView

class MachineController:
    # Constructor
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # Method for running the machine
    def run_machine(self):
        self.handle_file_upload(self.view.file_path.get())

    # Method for handling the file upload
    def handle_file_upload(self, file_path):
        self.model.set_path_file_directory(file_path)
        self.model.set_text_file_name(file_path.split("/")[-1])

        # Read the file
        with open(file_path, "r") as file:
            # Read the lines of the file
            lines = file.readlines()

            # Get the states
            states = lines[0].strip().split(",")
            self.model.set_states(states)

            # Get the alphabet
            alphabet = lines[1].strip().split(",")
            self.model.set_alphabet(alphabet)

            # Get the transitions
            transitions = []
            for i in range(2, len(lines) - 2):
                transitions.append(lines[i].strip().split(","))
            self.model.set_transitions(transitions)

            # Get the initial state
            initial_state = lines[-2].strip()
            self.model.set_initial_state(initial_state)

            # Get the final states
            final_states = lines[-1].strip().split(",")
            self.model.set_final_states(final_states)

            # Display the contents of the file
            self.view.display_contents(self.model)