
class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.delivered = False
        self.delivery_time = None

    def get_address(self):
        return self.address
    
    # Returns all package info
    def get_all_info(self):
        return f'ID: {self.id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, Deadline: {self.deadline}, Weight: {self.weight}'

    # Set delivery status and time delivered
    def set_delivered(self, time):
        self.delivered = True
        self.delivery_time = time

    # Get delivery status and time delivered
    def get_delivered(self):
        if self.delivered:
            return f'Delivered at {self.delivery_time}.'
        else:
            return 'Not delivered.'

    # Get deadline
    def get_deadline(self):
        return self.deadline

    # Get ID
    def get_id(self):
        return self.id