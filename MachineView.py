from tkinter import *
from tkinter import filedialog

class MachineView:
    def __init__(self):
        self.window = Tk()
        self.file_name = StringVar()
    
    def create_window(self, controller):
        self.controller = controller

        # Set the window properties
        self.window.title("Two-way Finite Automata")
        self.window.maxsize(800, 600)
        self.window.resizable(False, False)
        self.window.config(bg="CYAN4")

        # Create the frames
        self.top_frame = Frame(self.window, width=700, height=50, bg="SLATEGRAY2")
        self.top_frame.grid(row=0, column=0, padx=10, pady=10)

        self.middle_frame = Frame(self.window, width=700, height=500, bg="SLATEGRAY2")
        self.middle_frame.grid(row=1, column=0, padx=10, pady=5)

        # self.bottom_frame = Frame(self.window, width=700, height=50, bg="SLATEGRAY2")
        # self.bottom_frame.grid(row=2, column=0, padx=10, pady=5)

        # Create the frames within the middle frame
        self.left_frame = Frame(self.middle_frame, width=260, height=400, bg="LIGHTSKYBLUE3")
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)

        self.right_frame = Frame(self.middle_frame, width=400, height=400, bg="LIGHTSKYBLUE3")
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)

        # Create the label for the top frame
        self.top_label = Label(self.top_frame, text="Two-way Finite Automata", font=("Helvetica", 20, "bold"), bg="SLATEGRAY2")
        self.top_label.place(x=200, y=10)

        # Create the labels for the left frame
        self.left_label = Label(self.left_frame, text="Instructions", font=("Helvetica", 16, "bold"), bg="LIGHTSKYBLUE3")
        self.left_label.place(x=70, y=10)

        self.left_label_instruct = Label(self.left_frame, text="1. Click the 'Choose File' button to select a text file.\n2. Click the 'Run' button to run the machine.\n3. Click the 'Exit' button to exit the program.", font=("Helvetica", 12), bg="LIGHTSKYBLUE3")
        self.left_label_instruct.place(x=10, y=50)
        self.left_label_instruct.config(justify=LEFT)
        self.left_label_instruct.config(wraplength=240)     # When the texts are too long, the text will continue to the next line

        # Create the labels for the right frame
        self.right_label = Label(self.right_frame, text="INPUT", font=("Helvetica", 16, "bold"), bg="LIGHTSKYBLUE3")
        self.right_label.place(x=150, y=10)

        self.right_label_input = Label(self.right_frame, text="Textfile:", font=("Helvetica", 12), bg="LIGHTSKYBLUE3")
        self.right_label_input.place(x=10, y=50)

        # Entry field for the textfile
        self.right_entry_input = Entry(self.right_frame, textvariable=self.file_name, width=30, state="readonly")
        self.right_entry_input.place(x=80, y=50)

        # Create the buttons for the right frame
        # Button for choosing a file
        self.right_button_choose = Button(self.right_frame, text="Choose File", font=("Helvetica", 12), bg="LIGHTSKYBLUE3", command=self.upload_file)
        self.right_button_choose.place(x=280, y=40)

        # Button for running the machine is disabled by default
        self.right_button_run = Button(self.right_frame, text="Run the Machine", font=("Helvetica", 12), bg="LIGHTSKYBLUE3", state=DISABLED)
        self.right_button_run.place(x=150, y=100)

        # Button for exiting the program
        # self.right_button_exit = Button(self.right_frame, text="Exit", font=("Helvetica", 12), bg="LIGHTSKYBLUE3", command=self.window.destroy)
        # self.right_button_exit.place(x=180, y=150)

        # Create label for the output
        self.right_label_output = Label(self.right_frame, text="OUTPUT:", font=("Helvetica", 16, "bold"), bg="LIGHTSKYBLUE3")
        self.right_label_output.place(x=0, y=120)

        # Create a frame for the output
        self.right_output_frame = Frame(self.right_frame, width=380, height=200, bg="WHITE")
        self.right_output_frame.place(x=10, y=150)

        # Text for the output
        self.right_output_text = Text(self.right_output_frame, width=47, height=10, bg="LIGHT GRAY", wrap="word", state=DISABLED)
        self.right_output_text.place(x=0, y=0)
        self.right_output_text.pack()

        # Create label for the status
        self.right_label_status = Label(self.right_frame, text="STATUS:", font=("Helvetica", 12, "bold"), bg="LIGHTSKYBLUE3")
        self.right_label_status.place(x=0, y=315)

        # Create frame for Status frame
        self.right_status_frame = Frame(self.right_frame, width=380, height=50, bg="LIGHT GRAY")
        self.right_status_frame.place(x=10, y=340)

        # Text for the status
        self.right_status_text = Text(self.right_status_frame, width=380, height=50, bg="LIGHT GRAY", wrap="word", state=DISABLED)
        self.right_status_text.place(x=0, y=0)

        self.window.mainloop()

    # Method for uploading a file
    def upload_file(self):
        filepath = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        
        if not filepath:
            self.right_button_run.config(state=DISABLED)
            print("No such file or directory!")
            return
        else:
            print(filepath)
            filename = filepath.split("/")[-1]
            self.file_name.set(filename)
            self.right_button_run.config(state=NORMAL)
            self.right_button_run.config(command=lambda: self.controller.run_machine(filepath))
        
    # Method for displaying the contents of the file in the output frame
    def display_contents(self, model):
        # Clear the text
        self.right_output_text.config(state=NORMAL)
        self.right_output_text.delete(1.0, END)

        # Display the contents of the file
        self.right_output_text.insert(END, "Input String: " + str(model.get_input_string()) + "\n\n")
        
        self.right_output_text.insert(END, "States: " + str(model.get_states()) + "\n")
        self.right_output_text.insert(END, "Alphabets: " + str(model.get_alphabets()) + "\n")

        # Reformat the printing of the transitions
        self.right_output_text.insert(END, "Transitions: " + "\n")
        for transition in model.get_transitions():
            self.right_output_text.insert(END, str(transition) + " -> " + str(model.get_transitions()[transition]) + "\n")

        self.right_output_text.insert(END, "Initial State: " + str(model.get_initial_state()) + "\n")
        self.right_output_text.insert(END, "Accept State: " + str(model.get_final_state_accept()) + "\n")
        self.right_output_text.insert(END, "Reject State: " + str(model.get_final_state_reject()) + "\n")

    # Method for displaying the status of the machine
    def display_status(self, model):
        self.right_status_text.config(state=NORMAL)
        self.right_status_text.delete(1.0, END)

        if model.get_accepter_status():
            # Set the color of the text to green
            self.right_status_text.config(fg="green")
            self.right_status_text.insert(END, "The machine accepts the input string.")
        else:
            # Set the color of the text to red
            self.right_status_text.config(fg="red")
            self.right_status_text.insert(END, "The machine rejects the input string.")