# ID: 011890402, Name: Preston Backhaus

from truck import Truck
from packagedata import create_packages
from hashtable import HashTable

# Create packages, add to hashtable
packages = create_packages()
hashtable = HashTable(40)
for package in packages:
    hashtable.hash_insert(package)

# Packages with special instructions
# Truck 1 has packages that must be together
truck1_special = [hashtable.hash_lookup(13), hashtable.hash_lookup(14),
                    hashtable.hash_lookup(15), hashtable.hash_lookup(16),
                    hashtable.hash_lookup(19), hashtable.hash_lookup(20)]
# Truck 2 has packages that must be on truck 2
truck2_special = [hashtable.hash_lookup(3), hashtable.hash_lookup(18),
                  hashtable.hash_lookup(36), hashtable.hash_lookup(38)]
# Truck 3 has delayed packages, with the latest package loaded at 10:20 AM
truck3_special = [hashtable.hash_lookup(6), hashtable.hash_lookup(9),
                  hashtable.hash_lookup(25), hashtable.hash_lookup(28),
                  hashtable.hash_lookup(32)]

# Create Truck objects
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)
truck3.current_time = '10:20 AM'  # Truck 3 does not leave until 10:20 AM, when package 9 is loaded

# Add all special packages to trucks
for package in truck1_special:
    truck1.load_package(package)
for package in truck2_special:
    truck2.load_package(package)
for package in truck3_special:
    truck3.load_package(package)

# Add remaining packages to trucks, starting with truck 1 with package ID 1
for i in range(1, hashtable.size + 1):
    package = hashtable.hash_lookup(i)
    if package not in truck1_special + truck2_special + truck3_special:
        if not truck1.full:
            truck1.load_package(package)
        elif not truck2.full:
            truck2.load_package(package)
        elif not truck3.full:
            truck3.load_package(package)

'''
for package in truck1.packages:
    print(package.get_all_info())
print("\n")
for package in truck2.packages:
    print(package.get_all_info())
print("\n")
for package in truck3.packages:
    print(package.get_all_info())
'''

# Test nearest neighbor algorithm
truck1.test_nearest_neighbor()
print("Truck 1 test done \n\n")
truck2.test_nearest_neighbor()
print("Truck 2 test done\n\n")
truck3.test_nearest_neighbor()
print("Truck 3 test done\n\n")

# Print overall total distance
print(f"Total miles driven: {truck1.total_miles + truck2.total_miles + truck3.total_miles}.")
print(hashtable.get_all_status('8:25 AM'))