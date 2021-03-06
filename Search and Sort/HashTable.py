class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size  # List of nones
        self.data = [None] * self.size

    def put(self, key, data):   # Insert
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.re_hash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:   # For getting the next slots
                    next_slot = self.re_hash(next_slot, len(self.slots))
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else: self.data[next_slot] = data

    def hash_function(self, key, size): # We get the mod of the value
        return key % size

    def re_hash(self, old_hash, size):  # This method just setting the next slot for us to check it
        return (old_hash+1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.re_hash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
