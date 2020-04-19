class HashTable:
    def __int__(self, array_size):
        self.array_size = array_size
        self.array_bucket = [None for item in range(array_size)]

    # Create Hash Method

    def hash_key(self, key, count_collisions=0):
        char_bytes = key.encode()
        hashed = sum(char_bytes)
        return hashed + count_collisions

    def compress_key(self, hashed_key):
        return hashed_key % self.array_size

    def assign(self, key, value):
        array_index = self.compress_key(self.hash_key(key))
        current_array_value = self.aray_bucket[array_index]

        if current_array_value is None:
            self.array_bucket[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array_bucket[array_index] = [key, value]
            return

    def retrieve(self, key):
        array_index = self.compress_key(self.hash_key(key))
        possible_return_value = self.array_bucket[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

# Need to understand collisions

