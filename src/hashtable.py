from datetime import datetime


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Inserts package into correct bucket based on package id (key)
    def hash_insert(self, package):
        key = package.id
        index = int(key) % self.size  # Size is always 40 in this case
        if self.table[index] is None:  # If the index is empty, create a list
            self.table[index] = []
        self.table[index].append(package)  # Add to bucket
        
    # Search for package by id (key)
    def hash_lookup(self, key):
        index = int(key) % self.size
        if self.table[index] is not None:
            for package in self.table[index]:  # Finds package in bucket
                if package.id == str(key):
                    return package
        return None
    
    # Get all package statuses at a given time
    def get_all_status(self, time):
        # List to store statuses
        truck1_statuses = []
        truck2_statuses = []
        truck3_statuses = []
        check_time = datetime.strptime(time, '%I:%M %p')  # Convert time to datetime
        # Iterate over all packages in hash table
        for i in range(1, 41):
            package = self.hash_lookup(i)
            # Convert load and delivery time to datetime
            load_time = datetime.strptime(package.get_load_time(), '%I:%M %p')
            delivery_time = datetime.strptime(package.get_delivery_time(), '%I:%M %p')
            # Check if load time is after check time
            if load_time > check_time:
                if package.truck == 1:
                    truck1_statuses.append(f'Package {package.get_id()} is still at the hub.')
                elif package.truck == 2:
                    truck2_statuses.append(f'Package {package.get_id()} is still at the hub.')
                elif package.truck == 3:
                    truck3_statuses.append(f'Package {package.get_id()} is still at the hub.')
            # Check if delivery time is before check time
            elif delivery_time <= check_time:
                print(f'Package {package.get_id()} was delivered at {package.get_delivery_time()} to address {package.get_address()}.')
                if package.truck == 1:
                    truck1_statuses.append(f'Package {package.get_id()} was delivered at {package.get_delivery_time()} to address {package.get_address()}.')
                elif package.truck == 2:
                    truck2_statuses.append(f'Package {package.get_id()} was delivered at {package.get_delivery_time()} to address {package.get_address()}.')
                elif package.truck == 3:
                    truck3_statuses.append(f'Package {package.get_id()} was delivered at {package.get_delivery_time()} to address {package.get_address()}.')
            # If neither, package is on a truck/en route
            else:
                if package.truck == 1:
                    truck1_statuses.append(f'Package {package.get_id()} is en route.')
                elif package.truck == 2:
                    truck2_statuses.append(f'Package {package.get_id()} is en route.')
                elif package.truck == 3:
                    truck3_statuses.append(f'Package {package.get_id()} is en route.')
        return truck1_statuses, truck2_statuses, truck3_statuses

    # Get single package status at a given time
    def get_single_status(self, id, time):
        package = self.hash_lookup(id)
        check_time = datetime.strptime(time, '%I:%M %p')  # Convert time to datetime
        # Convert load and delivery time to datetime
        load_time = datetime.strptime(package.get_load_time(), '%I:%M %p')
        delivery_time = datetime.strptime(package.get_delivery_time(), '%I:%M %p')
        # Check if load time is after check time
        if load_time > check_time:
            return (f'Package {package.get_id()} was assigned to truck {package.truck}.\n'
                    f'Package is still at the hub.')
        # Check if delivery time is before check time
        elif delivery_time <= check_time:
            return (f'Package {package.get_id()} was assigned to truck {package.truck}.\n'
                    f'Package {package.get_id()} was delivered at {package.get_delivery_time()} to address {package.get_address()}.')
        # If neither, package is on a truck/en route
        else:
            return (f'Package {package.get_id()} was assigned to truck {package.truck}.\n'
                    f'Package is en route.')
