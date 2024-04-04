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

    # Look-up function to return all data components
    def hash_lookup(self, key):
        index = int(key) % self.size
        if self.table[index] is not None:
            for package in self.table[index]:  # Returns all requested package data
                return package.address, package.zip, package.city, package.deadline, package.weight, package.status
        return None
        
    # Search for package by id (key)
    def hash_search(self, key):
        index = int(key) % self.size
        if self.table[index] is not None:
            for package in self.table[index]:  # Finds package in bucket
                if package.id == str(key):
                    return package
        return None
    
    # Get all package statuses at a given time. Compares each package's delivery and load times with the given time
    def get_all_status(self, time):
        # List to store statuses
        truck1_statuses = []
        truck2_statuses = []
        truck3_statuses = []
        # List for packages that arrive late to depot
        late_packages = [6, 9, 25, 28, 32]
        late_statuses = []
        check_time = datetime.strptime(time, '%I:%M %p')  # Convert time to datetime
        # Iterate over all packages in hash table
        for i in range(1, 41):
            package = self.hash_search(i)
            # Convert load and delivery time to datetime
            load_time = datetime.strptime(package.get_load_time(), '%I:%M %p')
            delivery_time = datetime.strptime(package.get_delivery_time(), '%I:%M %p')
            # Convert times for packages that arrive late
            late_time = datetime.strptime('9:05 AM', '%I:%M %p')
            special_late_time = datetime.strptime('10:20 AM', '%I:%M %p')
            # Make sure package 9 is not loaded if the time is before 10:20 AM
            if i == 9 and special_late_time > check_time:
                late_statuses.append(f'Package {package.get_id()}, 300 State St, {package.get_city()}, '
                                     f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                     f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered, Address not yet changed.')
            # Make sure packages that arrive late are accounted for or not
            elif i in late_packages and late_time > check_time:
                late_statuses.append(f'Package {package.get_id()}, {package.get_address()}, {package.get_city()}, '
                                     f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                     f'Weight: {package.get_weight()}, Special note: {package.get_note()}, '
                                     f'Status: Has not arrived to the hub yet, Delivered: Not delivered.')
            # Check if load time is after check time
            elif load_time > check_time:
                package.set_at_hub()
                if package.get_id() == 9 and special_late_time > check_time:
                    truck3_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, 300 State St, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered.')
                elif package.truck == 1:
                    truck1_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered.')
                elif package.truck == 2:
                    truck2_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered.')
                elif package.truck == 3 and package.get_id() != 9:
                    truck3_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered.')
            # Check if delivery time is before check time
            elif delivery_time <= check_time:
                package.set_delivered(package.get_delivery_time())
                print(f'Package {package.get_id()} was delivered at {package.get_delivery_time()} to address {package.get_address()}. Deadline: {package.get_deadline()}.')
                if package.truck == 1:
                    truck1_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: {package.get_delivery_time()}.')
                elif package.truck == 2:
                    truck2_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: {package.get_delivery_time()}.')
                elif package.truck == 3:
                    truck3_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: {package.get_delivery_time()}.')
            # If neither, package is on a truck/en route
            else:
                package.set_en_route()
                if package.truck == 1:
                    truck1_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered.')
                elif package.truck == 2:
                    truck2_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered.')
                elif package.truck == 3:
                    truck3_statuses.append(f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered.')
        return truck1_statuses, truck2_statuses, truck3_statuses, late_statuses

    # Get single package status at a given time
    def get_single_status(self, id, time):
        package = self.hash_search(id)
        check_time = datetime.strptime(time, '%I:%M %p')  # Convert time to datetime
        # List for packages that arrive late to depot
        late_packages = ['6', '9', '25', '28', '32']
        # Convert load and delivery time to datetime
        load_time = datetime.strptime(package.get_load_time(), '%I:%M %p')
        delivery_time = datetime.strptime(package.get_delivery_time(), '%I:%M %p')
        # Convert times for packages that arrive late
        late_time = datetime.strptime('9:05 AM', '%I:%M %p')
        special_late_time = datetime.strptime('10:20 AM', '%I:%M %p')
        # Make sure package 9 is not loaded if the time is before 10:20 AM
        if id == '9' and special_late_time > check_time:
            return (f'Package {package.get_id()}, 300 State St, {package.get_city()}, '
                                 f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                 f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered, Address not yet changed.')
        # Make sure packages that arrive late are accounted for or not
        elif id in late_packages and late_time > check_time:
            return (f'Package {package.get_id()}, {package.get_address()}, {package.get_city()}, '
                                 f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                 f'Weight: {package.get_weight()}, Special note: {package.get_note()}, '
                                 f'Status: Has not arrived to the hub yet, Delivered: Not delivered.')
        # Check if load time is after check time
        elif load_time > check_time:
            package.set_at_hub()
            return (f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered.')
        # Check if delivery time is before check time
        elif delivery_time <= check_time:
            package.set_delivered(package.get_delivery_time())
            return (f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: {package.get_delivery_time()}.')
        # If neither, package is on a truck/en route
        else:
            package.set_en_route()
            return (f'Package {package.get_id()}, Truck: {package.get_truck()}, {package.get_address()}, {package.get_city()}, '
                                         f'{package.get_state()}, {package.get_zip()}, Deadline: {package.get_deadline()}, '
                                         f'Weight: {package.get_weight()}, Special note: {package.get_note()}, Status: {package.get_status()}, Delivered: Not delivered.')
