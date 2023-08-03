# Model 

class MachineModel:

    def __init__(self):
        pass


    
    # Getters
    def get_states(self):
        return self.__states

    def get_alphabet(self):
        return self.__alphabet
    
    def get_transitions(self):
        return self.__transitions
    
    def get_initial_state(self):
        return self.__initial_state
    
    def get_final_states(self):
        return self.__final_states
    
    def get_text_file_name():
        return MachineModel.__text_file_name
    
    def get_path_file_directory(self):
        return self.__path_file_directory
    
    # Setters
    def set_states(states):
        MachineModel.__states = states

    def set_alphabet(alphabet):
        MachineModel.__alphabet = alphabet

    def set_transitions(transitions):
        MachineModel.__transitions = transitions

    def set_initial_state(initial_state):
        MachineModel.__initial_state = initial_state

    def set_final_states(final_states):
        MachineModel.__final_states = final_states

    def set_text_file_name(text_file_name):
        MachineModel.__text_file_name = text_file_name

    def set_path_file_directory(path_file_directory):
        MachineModel.__path_file_directory = path_file_directory



    # Methods
