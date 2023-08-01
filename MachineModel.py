# Model 

class MachineModel:

    # Constructor
    def __init__(self):
        pass

    # Private Attributes
    __states = None
    __alphabet = None
    __transitions = None
    __initial_state = None
    __final_states = None
    __text_file_name = ""


    
    # Getters
    def get_states():
        return MachineModel.__states

    def get_alphabet():
        return MachineModel.__alphabet
    
    def get_transitions():
        return MachineModel.__transitions
    
    def get_initial_state():
        return MachineModel.__initial_state
    
    def get_final_states():
        return MachineModel.__final_states
    
    def get_text_file_name():
        return MachineModel.__text_file_name
    
    # Setters
    def set_states(self, states):
        MachineModel.__states = states

    def set_alphabet(self, alphabet):
        MachineModel.__alphabet = alphabet

    def set_transitions(self, transitions):
        MachineModel.__transitions = transitions

    def set_initial_state(self, initial_state):
        MachineModel.__initial_state = initial_state

    def set_final_states(self, final_states):
        MachineModel.__final_states = final_states

    def set_text_file_name(self, text_file_name):
        MachineModel.__text_file_name = text_file_name



    # Methods
