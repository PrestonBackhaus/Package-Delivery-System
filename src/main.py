# ID: 011890402, Name: Preston Backhaus

from truck import Truck
from packagedata import create_packages
from hashtable import HashTable

# Create packages, add to hashtable
packages = create_packages()
hashtable = HashTable(40)
for package in packages:
    hashtable.hash_insert(package)

# Create first Truck object
truck1 = Truck(1)

# Add all packages to truck
for i in range(1, 17):
    package = hashtable.hash_lookup(i)
    if package:
        truck1.load_package(package)

for package in truck1.get_all_packages():
    print(package.get_all_info())

truck1.test_nearest_neighbor()
