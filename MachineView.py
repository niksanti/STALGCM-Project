from tkinter import *
from tkinter import filedialog

class MachineView:
    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.file_path = StringVar()
        self.file_name = StringVar()
    
    def create_window(self):
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
        self.right_entry_input = Entry(self.right_frame, textvariable=self.file_name, width=30)
        self.right_entry_input.place(x=80, y=50)

        # Create the buttons for the right frame
        # Button for choosing a file
        self.right_button_choose = Button(self.right_frame, text="Choose File", font=("Helvetica", 12), bg="LIGHTSKYBLUE3", command=self.upload_file)
        self.right_button_choose.place(x=280, y=40)

        # Button for running the machine is disabled by default
        self.right_button_run = Button(self.right_frame, text="Run the Machine", font=("Helvetica", 12), bg="LIGHTSKYBLUE3", command=self.controller.run_machine, state=DISABLED)
        self.right_button_run.place(x=150, y=100)

        # Button for exiting the program
        # self.right_button_exit = Button(self.right_frame, text="Exit", font=("Helvetica", 12), bg="LIGHTSKYBLUE3", command=self.window.destroy)
        # self.right_button_exit.place(x=180, y=150)

        # Create a frame for the output
        self.right_output_frame = Frame(self.right_frame, width=380, height=200, bg="WHITE")
        self.right_output_frame.place(x=10, y=150)

        self.window.mainloop()

    # Method for uploading a file
    def upload_file(self):
        filepath = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        filename = filepath.split("/")[-1]
        self.file_path.set(filepath)
        self.file_name.set(filename)
        self.check_file_path()

    def check_file_path(self):
        if self.file_path.get() != "":
            self.right_button_run.config(state=NORMAL)
        else:
            self.right_button_run.config(state=DISABLED)

    # Method for displaying the contents of the file in the output frame
    def display_contents(self, model):
        # Check the console
        # print(model.get_states())
        # print(model.get_alphabet())
        # print(model.get_transitions())
        # print(model.get_initial_state())
        # print(model.get_final_states())

        self.right_output_text = Text(self.right_output_frame, width=45, height=10, bg="WHITE")
        self.right_output_text.place(x=0, y=0)
        self.right_output_text.pack()

        self.right_output_text.insert(END, "STATES: " + ", ".join(model.get_states()) + "\n")
        self.right_output_text.insert(END, "ALPHABET: " + ", ".join(model.get_alphabet()) + "\n")
        self.right_output_text.insert(END, "TRANSITIONS: " + "\n")
        for transition in model.get_transitions():
            self.right_output_text.insert(END, ", ".join(transition) + "\n")
        self.right_output_text.insert(END, "INITIAL STATE: " + model.get_initial_state() + "\n")
        self.right_output_text.insert(END, "FINAL STATES: " + ", ".join(model.get_final_states()) + "\n")
        