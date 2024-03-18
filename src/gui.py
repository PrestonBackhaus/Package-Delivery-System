import tkinter as tk


class GUI(tk.Frame):
    def __init__(self, master=None):
        # Initialize frame
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)

        # Call methods
        self.create_widgets()

    def create_widgets(self):
        # Exit button
        self.exit = tk.Button(self, text="Exit", command=self.master.destroy)
        self.exit.pack(side="bottom")

        # Title
        self.title = tk.Label(self, text="WGU Package Delivery")
        self.title.pack(side="top", pady=10)

        # Truck 1 labels
        self.truck1_frame = tk.Frame(self)
        self.truck1_frame.pack(fill=tk.X, padx=5, pady=10)
        self.truck1_label = tk.Label(self.truck1_frame, text="Truck 1")
        self.truck1_label.grid(row=0, column=0)
        self.truck1_current_location = tk.Label(self.truck1_frame, text="Current Location: ")
        self.truck1_current_location.grid(row=1, column=0, sticky=tk.E)
        self.truck1_next_location = tk.Label(self.truck1_frame, text="Next Location: ")
        self.truck1_next_location.grid(row=2, column=0, sticky=tk.E)
        self.truck1_distance = tk.Label(self.truck1_frame, text="Total Distance: ")
        self.truck1_distance.grid(row=3, column=0, sticky=tk.E)

        # Truck 2 labels
        self.truck2_frame = tk.Frame(self)
        self.truck2_frame.pack(fill=tk.X, padx=5, pady=10)
        self.truck2_label = tk.Label(self.truck2_frame, text="Truck 2")
        self.truck2_label.grid(row=0, column=0)
        self.truck2_current_location = tk.Label(self.truck2_frame, text="Current Location: ")
        self.truck2_current_location.grid(row=1, column=0, sticky=tk.E)
        self.truck2_next_location = tk.Label(self.truck2_frame, text="Next Location: ")
        self.truck2_next_location.grid(row=2, column=0, sticky=tk.E)
        self.truck2_distance = tk.Label(self.truck2_frame, text="Total Distance: ")
        self.truck2_distance.grid(row=3, column=0, sticky=tk.E)

        # Truck 3 labels
        self.truck3_frame = tk.Frame(self)
        self.truck3_frame.pack(fill=tk.X, padx=5, pady=10)
        self.truck3_label = tk.Label(self.truck3_frame, text="Truck 3")
        self.truck3_label.grid(row=0, column=0)
        self.truck3_current_location = tk.Label(self.truck3_frame, text="Current Location: ")
        self.truck3_current_location.grid(row=1, column=0, sticky=tk.E)
        self.truck3_next_location = tk.Label(self.truck3_frame, text="Next Location: ")
        self.truck3_next_location.grid(row=2, column=0, sticky=tk.E)
        self.truck3_distance = tk.Label(self.truck3_frame, text="Total Distance: ")
        self.truck3_distance.grid(row=3, column=0, sticky=tk.E)

    def update_truck1(self, current_location, next_location, distance):
        self.truck1_current_location.config(text=f"Current Location: {current_location}")
        self.truck1_next_location.config(text=f"Next Location: {next_location}")
        self.truck1_distance.config(text=f"Total Distance: {distance}")

    def update_truck2(self, current_location, next_location, distance):
        self.truck2_current_location.config(text=f"Current Location: {current_location}")
        self.truck2_next_location.config(text=f"Next Location: {next_location}")
        self.truck2_distance.config(text=f"Total Distance: {distance}")

    def update_truck3(self, current_location, next_location, distance):
        self.truck3_current_location.config(text=f"Current Location: {current_location}")
        self.truck3_next_location.config(text=f"Next Location: {next_location}")
        self.truck3_distance.config(text=f"Total Distance: {distance}")

# Test GUI
root = tk.Tk()
root.geometry("800x600")
app = GUI(master=root)
app.mainloop()
