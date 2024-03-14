class Truck:
    # Initialize truck with an id (1-3), empty package list, and starting location
    def __init__(self, id):
        self.id = id
        self.packages = []
        self.current_location = "4001 South 700 East"  # WGU hub

    # Load packages into the truck
    def load_package(self, package):
        if len(self.packages) < 16:
            self.packages.append(package)
        else:
            return "Truck is already full."

    # Get all packages in truck
    def get_all_packages(self):
        return self.packages

    # Deliver package and delete it from truck
    def deliver_pacakge(self, package):
        self.current_location = package.get_address()
        package.delivered = True
        self.packages.remove(package)

    # Get current location
    def get_current_location(self):
        return self.current_location
