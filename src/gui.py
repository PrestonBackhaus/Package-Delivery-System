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
        self.truck1_label = tk.Label(self, text="Truck 1")
        self.truck1_label.pack(anchor='w', padx=5, pady=3)
        self.truck1_current_location = tk.Label(self, text="Current Location: ")
        self.truck1_current_location.pack(anchor='w', padx=5, pady=3)
        self.truck1_next_location = tk.Label(self, text="Next Location: ")
        self.truck1_next_location.pack(anchor='w', padx=5, pady=3)
        self.truck1_distance = tk.Label(self, text="Distance: ")
        self.truck1_distance.pack(anchor='w', padx=5, pady=3)

    def update_truck1(self, current_location, next_location, distance):
        self.truck1_current_location.config(text=f"Current Location: {current_location}")
        self.truck1_next_lcoation.config(text=f"Next Location: {next_location}")
        self.truck1_distance.config(text=f"Distance: {distance}")

# Test GUI
root = tk.Tk()
root.geometry("800x600")
app = GUI(master=root)
app.mainloop()
