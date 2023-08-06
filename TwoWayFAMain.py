# Main

from MachineModel import MachineModel
from MachineController import MachineController
from MachineView import MachineView 

def TwoWayFAMain():
    model = MachineModel()
    view = MachineView()
    controller = MachineController(model, view)
    
    view.create_window(controller=controller)  


if __name__ == "__main__":
    TwoWayFAMain()