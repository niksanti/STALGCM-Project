# Main

from MachineModel import MachineModel
from MachineController import MachineController
from MachineView import MachineView 

def TwoWayFAMain():
    model = MachineModel()                          # Create an object of the model class
    controller = MachineController(model, None)     # Create an object of the controller class
    view = MachineView(controller)                  # Create an object of the view class
    
    view.create_window()                            # Create the window

if __name__ == "__main__":
    TwoWayFAMain()