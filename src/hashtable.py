class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Inserts package into correct bucket based on package id (key)
    def hash_insert(self, package):
        key = package.id
        index = int(key) % self.size  # Always 40 in this case
        if self.table[index] is None:  # If the index is empty, create a list
            self.table[index] = []
        self.table[index].append(package)  # Add to bucket
        
    # Search for package by id (key)
    def hash_lookup(self, key):
        index = int(key) % self.size
        if self.table[index] is not None:
            for package in self.table[index]:
                if package.id == key:
                    return package
        return None
    
    