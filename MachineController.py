# Controller for the machine

from tkinter import END, filedialog

class MachineController:

    # Constructor
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # Set up the button
        self.view.browseButton.config(command=self.browseFiles)
        self.view.runButton.config(command=self.runMachine)

    # Browse files from local machine
    def browseFiles(self):
        self.view.filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        # Get only the filename not the path
        self.view.filename = self.view.filename.split("/")[-1]
        self.model.set_text_file_name(self.view.filename)
        self.view.rightBodyInputField.insert(END, self.view.filename)
        


    # Run the machine
    def runMachine(self):
        # read the contents of the text file
        file = open(self.view.filename, "r")
        contents = file.read()
        file.close()


    

    
