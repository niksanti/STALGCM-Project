# Model 

class MachineModel:
    # Constructor
    def __init__(self):
        self._states = []
        self._alphabet = []
        self._transitions = []
        self._initial_state = ""
        self._final_states = []
        self._text_file_name = ""
        self._path_file_directory = ""
    
    # Getters
    def get_states(self):
        return self._states

    def get_alphabet(self):
        return self._alphabet
    
    def get_transitions(self):
        return self._transitions
    
    def get_initial_state(self):
        return self._initial_state
    
    def get_final_states(self):
        return self._final_states
    
    def get_text_file_name(self):
        return self._text_file_name
    
    def get_path_file_directory(self):
        return self._path_file_directory
    
    # Setters
    def set_states(self, states):
        self._states = states

    def set_alphabet(self, alphabet):
        self._alphabet = alphabet

    def set_transitions(self, transitions):
        self._transitions = transitions

    def set_initial_state(self, initial_state):
        self._initial_state = initial_state

    def set_final_states(self, final_states):
        self._final_states = final_states

    def set_text_file_name(self, text_file_name):
        self._text_file_name = text_file_name

    def set_path_file_directory(self, path_file_directory):
        self._path_file_directory = path_file_directory