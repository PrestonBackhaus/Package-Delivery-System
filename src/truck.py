import distancedata
from hashtable import HashTable
from package import Package


class Truck:
    # Distance and address data
    addresses = distancedata.create_addresses()
    distances = distancedata.create_distances()
    # print(addresses)
    # print(distances)

    # Initialize truck with an id (1-3), empty package list, and starting location
    def __init__(self, id):
        self.id = id
        self.packages = []
        self.delivered_packages = []
        self.current_location = "4001 South 700 East"  # WGU hub
        self.current_time = '8:00 AM'
        self.total_miles = 0
        self.started_flag = False
        self.full = False

    # Load packages into the truck
    def load_package(self, package):
        if not self.full:  # Add as long as the truck is not full
            self.packages.append(package)
            package.set_en_route()  # Set package status to en route
            package.set_load_time(self.current_time)  # Set package load time to current time
            if len(self.packages) == 16:  # If the truck has 16 packages, it is full
                self.full = True

    # Get all packages in truck
    def get_all_packages(self):
        return self.packages

    # Deliver package and delete it from truck
    def deliver_package(self, package):
        self.current_location = package.get_address()
        package.delivered = True
        self.delivered_packages.append(package)  # Add to keep track of delivered packages
        package.set_delivered(self.current_time)  # Set package status to delivered, add current time
        self.packages.remove(package)

    # Get current location
    def get_current_location(self):
        return self.current_location

    # Nearest Neighbor Greedy algorithm for finding the shortest distance
    def nearest_neighbor(self):
        # Temp package to hold the current location for comparison with the next package
        temp_package = Package("0", self.current_location, "", "", "", "", "", "N/A")
        while len(self.packages) > 0:  # While there are still packages
            next_package = None
            shortest = 1000
            for package in self.packages:  # Iterate through every package
                distance = self.distance_between(temp_package, package)  # Get the distance between packages
                if distance is None:
                    print(distance)
                    print(temp_package.get_address(), package.get_address())
                if distance < shortest:  # Set the shortest distance and next package
                    shortest = distance
                    next_package = package
            self.current_location = next_package.get_address()
            temp_package = next_package  # Set the temp package to the next package
            time_to_deliver = shortest / 18  # Time to deliver package in hours
            self.current_time = self.update_time(time_to_deliver)  # Update time
            self.deliver_package(next_package)  # Deliver package, deleting it from the truck
            self.total_miles = round(self.total_miles + shortest, 1)  # Add distance to total miles, round to 1 decimal
            print(f"Package with ID {next_package.get_id()} delivered to {next_package.get_address()}.")
            print(f"Distance driven: {shortest}.")
            print(f"Total miles driven so far: {self.total_miles}.")
            print(f"Current time: {self.current_time}.")
            print(f"Current location: {self.current_location}.\n")
            self.started_flag = True
        return self.total_miles

    # Find distance between two addresses
    def distance_between(self, package1, package2):
        address1 = package1.get_address()
        address2 = package2.get_address()
        index1 = self.addresses.index(address1)  # Get index of address in list
        index2 = self.addresses.index(address2)
        if index1 == index2:  # If the addresses are the same, it travels no distance
            return 0.0
        if index2 == 1:  # Special case for when the address is one index after the hub
            index2 += 1
        if not self.started_flag: # For the first run, the horizontal index starts at 0
            if index1 < index2:  # Always start with the smaller index
                return self.distances[index2 - 1][index1]
            else:
                return self.distances[index1 - 1][index2]
        else: # For the second run on, the index starts at 1
            index1 -= 1
            index2 -= 1
            if index1 < index2:
                return self.distances[index2][index1]
            else:
                return self.distances[index1][index2]

    # Updates the time in datetime format by converting the decimal hours into hours and minutes
    def update_time(self, time):
        # Convert time (hours in decimal format) to hours and minutes
        hours = int(time)
        minutes = int((time - hours) * 60)
        # Convert current time into hours, minutes, and AM/PM
        current_hours, current_minutes = self.current_time.split(":")
        current_minutes, am_pm = current_minutes.split(" ")
        current_hours = int(current_hours)
        current_minutes = int(current_minutes)
        # Add the time to the current time
        current_hours += hours
        current_minutes += minutes
        # If minutes over 60
        if current_minutes >= 60:
            current_minutes -= 60
            current_hours += 1
        # If hours over 12, change AM to PM
        if current_hours >= 12:
            current_hours -= 12
            am_pm = "PM"
        else:
            am_pm = "AM"
        # Convert time back to a string, keeping minutes to two digits
        self.current_time = f"{current_hours}:{current_minutes:02d} {am_pm}"
        return self.current_time

    # Test to make sure the nearest neighbor algorithm works
    def test_nearest_neighbor(self):
        # Run nearest neighbor algorithm which ends up returning the total miles
        total_miles = round(self.nearest_neighbor(), 1)
        print(f"Total miles overall: {total_miles}. Current time: {self.current_time}.")
        # Print the packages in order of delivery
        for package in self.delivered_packages:
            print(package.get_all_info())

