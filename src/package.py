
class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time = None
        self.load_time = None
        self.truck = None
        self.priority = False
        self.special = ''

    # Returns address
    def get_address(self):
        return self.address

    # Set package address
    def set_address(self, address):
        self.address = address

    # Get city
    def get_city(self):
        return self.city

    # Set city
    def set_city(self, city):
        self.city = city

    # Get state
    def get_state(self):
        return self.state

    # Set state
    def set_state(self, state):
        self.state = state

    # Returns all package info
    def get_all_info(self):
        return (f'ID: {self.id}, Address: {self.address}, City: {self.city}, State: {self.state}, '
                f'Zip: {self.zip}, Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status}')

    # Set delivery status to 'Delivered' and set time delivered
    def set_delivered(self, time):
        self.status = 'Delivered'
        self.delivery_time = time

    # Set delivery status to 'At the hub'
    def set_at_hub(self):
        self.status = 'At the hub'

    # Set delivery status to 'En route'
    def set_en_route(self):
        self.status = 'En route'

    # Get delivery status and time delivered
    def get_status(self):
        if self.status == 'Delivered':
            return f'Delivered at {self.delivery_time}.'
        elif self.status == 'At the hub':
            return f'Package is at the hub.'
        elif self.status == 'En route':
            return f'Package is en route.'
        else:
            return f'Package is not delivered.'

    # Get deadline
    def get_deadline(self):
        return self.deadline

    # Get ID
    def get_id(self):
        return self.id

    # Set delivery time
    def set_delivery_time(self, time):
        self.delivery_time = time

    # Get delivery time
    def get_delivery_time(self):
        return self.delivery_time

    # Set load time
    def set_load_time(self, time):
        self.load_time = time

    # Get load time
    def get_load_time(self):
        return self.load_time

    # Get the truck the package is on
    def get_truck(self):
        return self.truck

    # Get special instructions (only set for 9:05 AM arrival)
    def get_special(self):
        return self.special