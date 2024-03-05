class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [] * size

    def HashInsert(self, table, item):
        index = int(item[0])
        table[index] = item
        
    def HashSearch(self, table, key):
        index = int(key)
        return table[index]