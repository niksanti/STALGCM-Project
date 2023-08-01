from tkinter import *
from tkinter import filedialog

import MachineController as mc
import MachineModel as mm

class MachineView:

    # Create root window
    window = Tk()

    # Constants
    filename = ""

    # Set up the GUI window
    window.title("Two-Way Finite Automata")         # Title of the GUI window
    window.maxsize(800, 600)                        # Max Size of the GUI window
    window.resizable(0, 0)                          # Disable resizing of the GUI window
    window.config(bg="cyan4")                        # Background color of the GUI window

    # Contents of the GUI window
    upperFrame = Frame(window, width=700, height=50, bg="SlateGray2")     # Upper frame
    upperFrame.grid(row=0, column=0, padx=10, pady=5)               # Position of the upper frame  

    bodyFrame = Frame(window, width=700, height=500, bg="SlateGray2")     # Body frame    
    bodyFrame.grid(row=1, column=0, padx=10, pady=5)                # Position of the body frame

    # Create frame within the body frame
    leftBodyFrame = Frame(bodyFrame, width=260, height=400, bg="LightSkyBlue3")    # Left Body frame
    leftBodyFrame.grid(row=0, column=0, padx=10, pady=5)                    # Position

    rightBodyFrame = Frame(bodyFrame, width=400, height=400, bg="LightSkyBlue3")    # Right Body frame
    rightBodyFrame.grid(row=0, column=1, padx=10, pady=5)                   # Position

    # Create label for the upper frame that maximizes the whole upper frame
    upperLabel = Label(upperFrame, text="Two-Way Finite Automata", font=("Arial", 20, "bold"), bg="SlateGray2")
    upperLabel.place(x=200, y=10)

    # Create label for the left body frame that maximizes the whole left body frame
    # This label contains the set of instructions for the user
    leftBodyLabel = Label(leftBodyFrame, text="Instructions", font=("Arial", 20, "bold"), bg="Lightskyblue3")
    leftBodyLabel.place(x=50, y=10)

    leftBodyInstr = Label(leftBodyFrame, text="1. Enter the number of states\n2. Enter the number of input symbols\n3. Enter the input symbols\n4. Enter the number of final states\n5. Enter the final states\n6. Enter the number of transitions\n7. Enter the transitions", font=("Arial", 10), bg="Lightskyblue3")
    leftBodyInstr.place(x=10, y=50)
    # align the text to the left
    leftBodyInstr.config(justify=LEFT)

    # Create label for the right body frame that maximizes the whole right body frame
    # This label contains the input fields for the user
    rightBodyLabel = Label(rightBodyFrame, text="Input Fields", font=("Arial", 20, "bold"), bg="Lightskyblue3")
    rightBodyLabel.place(x=100, y=10)

    # Create field to upload a text file as user input
    rightBodyInput = Label(rightBodyFrame, text="Upload a text file as input: ", font=("Arial", 10), bg="Lightskyblue3")
    rightBodyInput.place(x=10, y=50)

    # Create entry field for user to upload text file from local machine
    rightBodyInputField = Entry(rightBodyFrame, width=30, borderwidth=2)
    rightBodyInputField.place(x=200, y=50)

    # Create button for user to browse files from local machine
    browseButton = Button(rightBodyFrame, text="Browse Files", font=("Arial", 10), bg="SlateGray2", state="normal")
    browseButton.place(x=200, y=80)

    # The create run button for user to run the machine and it is disabled by default
    runButton = Button(rightBodyFrame, text="Run Machine", font=("Arial", 10), bg="SlateGray2", state="disabled")
    runButton.place(x=300, y=80)


    # Create field to display the output of the machine
    rightBodyOutput = Label(rightBodyFrame, text="Output: ", font=("Arial", 10), bg="Lightskyblue3")
    rightBodyOutput.place(x=10, y=120)
    
    # Output frame
    outputFrame = Frame(rightBodyFrame, width=380, height=230, bg="white")
    outputFrame.place(x=10, y=150)

