# Main 

# Call the view.py to display the GUI
from MachineView import *

# Call the model.py to perform the operations
from MachineModel import *

# Call the controller.py to control the flow of the program
from MachineController import *

# Create an object of the view class
view = MachineView()

# Create an object of the model class
model = MachineModel()

# Create an object of the controller class
controller = MachineController(view, model)


# Run the program
view.window.mainloop()