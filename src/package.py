
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

    def get_address(self):
        return self.address
    
    # Returns all package info
    def get_all_info(self):
        return f'ID: {self.id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status}'

    # Set delivery status and time delivered
    def set_delivered(self, time):
        self.status = 'Delivered'
        self.delivery_time = time

    # Get delivery status and time delivered
    def get_status(self):
        if self.status == 'Delivered':
            return f'Delivered at {self.delivery_time}.'
        elif self.status == 'At the hub':
            return f'At the hub. Current time: {self.delivery_time}.'
        elif self.status == 'En route':
            return f'En route. Current time: {self.delivery_time}.'
        else:
            return f'Not delivered. Current time: {self.delivery_time}.'

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