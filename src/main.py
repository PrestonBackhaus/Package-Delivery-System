# ID: 011890402, Name: Preston Backhaus

from truck import Truck
from packagedata import create_packages
from hashtable import HashTable
from gui import GUI
import tkinter as tk

# Create packages, add to hashtable
packages = create_packages()
hashtable = HashTable(40)
for package in packages:
    hashtable.hash_insert(package)
    if package.get_id() in ['6', '25', '28', '32']:
        package.special = '9:05 AM'

# Packages with special instructions or failing time constraints
# Truck 1 has packages that must be together
truck1_special = [hashtable.hash_search(13), hashtable.hash_search(14),
                  hashtable.hash_search(15), hashtable.hash_search(16),
                  hashtable.hash_search(19), hashtable.hash_search(20),
                  hashtable.hash_search(29), hashtable.hash_search(34),
                  hashtable.hash_search(30), hashtable.hash_search(37),
                  hashtable.hash_search(31), hashtable.hash_search(17),
                  hashtable.hash_search(10), hashtable.hash_search(40)]
# Truck 2 has packages that must be on truck 2
truck2_special = [hashtable.hash_search(3), hashtable.hash_search(6),
                  hashtable.hash_search(18), hashtable.hash_search(25),
                  hashtable.hash_search(36), hashtable.hash_search(38)]
# Truck 3 has delayed packages, with the latest package loaded at 10:20 AM
truck3_special = [hashtable.hash_search(9),
                  hashtable.hash_search(28),
                  hashtable.hash_search(32)]

# Create Truck objects
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)
truck2.current_time = '9:05 AM'  # Truck 2 will carry package 6
truck3.current_time = '10:20 AM'  # Truck 3 does not leave until 10:20 AM, when package 9 is loaded

# Add all special packages to trucks
for package in truck1_special:
    truck1.load_package(package)
for package in truck2_special:
    truck2.load_package(package)
if truck3.current_time == '10:20 AM':  # Change pacakge 9's address when truck3's time reaches 10:20 AM
    package9 = hashtable.hash_search(9)
    package9.set_address('410 S State St')
for package in truck3_special:
    truck3.load_package(package)

# Add remaining packages to trucks, starting with truck 1 with package ID 1
for i in range(1, hashtable.size + 1):
    package = hashtable.hash_search(i)
    # Search through all special packages to see if the package is already on a truck
    if package not in truck1_special + truck2_special + truck3_special:
        if not truck1.full:
            truck1.load_package(package)
        elif not truck2.full:
            truck2.load_package(package)
        elif not truck3.full:
            truck3.load_package(package)

# Run nearest neighbor algorithm for each truck
truck1.nearest_neighbor()  # Truck 1 driver finishes before 10:20 AM
truck2.nearest_neighbor()
truck3.nearest_neighbor()  # Truck 3 starts at 10:20 AM for the latest available packages

root = tk.Tk()
root.geometry("1200x800")
gui = GUI(root, hashtable, truck1, truck2, truck3)
root.mainloop()

