# Controller for the machine

class MachineController:
    # Constructor
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # Method for running the machine
    def run_machine(self, file_path):
        self.model.handle_file_upload(file_path)
        self.view.display_contents(self.model)
        self.view.display_status(self.model)  