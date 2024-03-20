import tkinter as tk


class GUI(tk.Frame):
    def __init__(self, master=None, hashtable=None, truck1=None, truck2=None, truck3=None):
        # Initialize frame
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)

        # Store hashtable and trucks
        self.hashtable = hashtable
        self.truck1 = truck1
        self.truck2 = truck2
        self.truck3 = truck3

        # Call methods
        self.create_widgets()

    def create_widgets(self):
        # Exit button
        self.exit = tk.Button(self, text="Exit", command=self.master.destroy)
        self.exit.place(relx=0.5, rely=0.99, anchor='s')

        # Title
        self.title = tk.Label(self, text="WGU Package Delivery System")
        self.title.place(relx=0.5, rely=0.01, anchor='n')

        # Print all status with total miles driven
        self.status_mileage_label = tk.Label(self, text="Get all statuses and mileage:")
        self.status_mileage_label.place(relx=0.02, rely=0.2, anchor='nw')

        # Button for status and mileage
        self.status_mileage_button = tk.Button(self, text="Go", command=self.display_all_status_mileage)
        self.status_mileage_button.place(relx=0.02, rely=0.25, anchor='nw')

        # Print a single package's status at a given time
        self.single_status_label = tk.Label(self, text="Get a single package's status at a given time:\n"
                                                       "(Enter in format '8:00 AM')")
        self.single_status_label.place(relx=0.02, rely=0.4, anchor='nw')

        # Label for ID
        self.single_id_label = tk.Label(self, text="ID:")
        self.single_id_label.place(relx=0.02, rely=0.48, anchor='nw')

        # Input for ID
        self.single_id = tk.Entry(self, width=2)
        self.single_id.place(relx=0.05, rely=0.48, anchor='nw')

        # Label for time
        self.single_time_label = tk.Label(self, text="Time:")
        self.single_time_label.place(relx=0.1, rely=0.48, anchor='nw')

        # Input for time
        self.single_time = tk.Entry(self, width=8)
        self.single_time.place(relx=0.16, rely=0.48, anchor='nw')

        # Button for single status, uses single_id and single_time as parameters
        self.single_status_button = tk.Button(self, text="Go", command=lambda:
        self.display_single_status(self.single_id.get(), self.single_time.get()))
        self.single_status_button.place(relx=0.02, rely=0.54, anchor='nw')

        # Print all package statuses at a given time
        self.all_status_label = tk.Label(self,
                                         text="Get all package statuses at a given time:\n(Enter in format '8:00 AM')")
        self.all_status_label.place(relx=0.02, rely=0.7, anchor='nw')

        # Input for time
        self.all_time = tk.Entry(self, width=8)
        self.all_time.place(relx=0.08, rely=0.78, anchor='nw')

        # Button for all statuses, uses all_time as parameter
        self.all_status_button = tk.Button(self, text="Go",
                                           command=lambda: self.display_all_status(self.all_time.get()))
        self.all_status_button.place(relx=0.02, rely=0.84, anchor='nw')

        # Label for time
        self.all_time_label = tk.Label(self, text="Time:")
        self.all_time_label.place(relx=0.02, rely=0.78, anchor='nw')

        # Text box for all status and mileage
        self.all_results_text = tk.Text(self, width=100, height=48)
        self.all_results_text.place(relx=0.3, rely=0.1, anchor='nw')

    # Display all statuses and mileage, attached to first button
    def display_all_status_mileage(self):
        # Clear the text box in case it was previously filled
        self.all_results_text.delete(1.0, tk.END)
        # Get statuses (late_statuses is unused because delivery has finished)
        # 3:00 PM is a placeholder later than any delivery time
        truck1_statuses, truck2_statuses, truck3_statuses, late_statuses = self.hashtable.get_all_status('3:00 PM')
        # Convert status list to a string for display on label
        truck1_statuses_string = '\n'.join(truck1_statuses)
        truck2_statuses_string = '\n'.join(truck2_statuses)
        truck3_statuses_string = '\n'.join(truck3_statuses)
        # Get truck mileage for each truck
        truck1_miles = self.truck1.total_miles
        truck2_miles = self.truck2.total_miles
        truck3_miles = self.truck3.total_miles
        total_miles = truck1_miles + truck2_miles + truck3_miles  # Total mileage of the whole delivery system
        # Display package statuses and mileage for each truck
        self.all_results_text.insert(tk.END, f"Truck 1 statuses:\n{truck1_statuses_string}\n"
                                             f"Truck 2 statuses:\n{truck2_statuses_string}\n"
                                             f"Truck 3 statuses:\n{truck3_statuses_string}\n"
                                             f"Truck 1 miles: {truck1_miles}\n"
                                             f"Truck 2 miles: {truck2_miles}\n"
                                             f"Truck 3 miles: {truck3_miles}\n"
                                             f"Total miles driven: {total_miles}.")

    # Display single status at given time, attached to second button
    def display_single_status(self, id, time):
        # Clear
        self.all_results_text.delete(1.0, tk.END)
        # Get status
        status = self.hashtable.get_single_status(id, time)
        # Display status
        self.all_results_text.insert(tk.END, status)

    # Display all statuses at given time, attached to third button
    def display_all_status(self, time):
        # Clear
        self.all_results_text.delete(1.0, tk.END)
        # Get statuses
        truck1_statuses, truck2_statuses, truck3_statuses, late_statuses = self.hashtable.get_all_status(time)
        # Convert status list to a string for display on label
        truck1_statuses_string = '\n'.join(truck1_statuses)
        truck2_statuses_string = '\n'.join(truck2_statuses)
        truck3_statuses_string = '\n'.join(truck3_statuses)
        late_statuses_string = '\n'.join(late_statuses)
        # Display statuses
        self.all_results_text.insert(tk.END, f"Truck 1 statuses:\n{truck1_statuses_string}\n"
                                             f"Truck 2 statuses:\n{truck2_statuses_string}\n"
                                             f"Truck 3 statuses:\n{truck3_statuses_string}\n"
                                             f"Packages unable to be loaded at this time:\n{late_statuses_string}")

