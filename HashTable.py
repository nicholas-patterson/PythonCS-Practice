class HashTable(object):
    def __init__(self, array_size):
        self.array_size = array_size
        self.array_bucket = [None for item in range(array_size)]

    def hash_key(self, key, count_collisions=0):
        char_bytes = key.encode()
        hashed = sum(char_bytes)
        return hashed + count_collisions

    def compress_key(self, hashed_key):
        return hashed_key % self.array_size

    def assign(self, key, value):
        array_index = self.compress_key(self.hash_key(key))
        current_array_value = self.array_bucket[array_index]

        if current_array_value is None:
            self.array_bucket[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array_bucket[array_index] = [key, value]
            return

        # We have collisions

        number_collisions = 1

        while current_array_value[0] != key:
            new_hash_code = self.hash_key(key, number_collisions)
            new_array_index = self.compress_key(new_hash_code)
            current_array_value = self.array_bucket[new_array_index]

            if current_array_value is None:
                self.array_bucket[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array_bucket[new_array_index] = [key, value]
                return

            number_collisions += 1
            print("???", number_collisions)

    def retrieve(self, key):
        array_index = self.compress_key(self.hash_key(key))
        possible_return_value = self.array_bucket[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        while possible_return_value[0] != key:
            new_hash_code = self.hash_key(key, retrieval_collisions)
            new_array_index = self.compress_key(new_hash_code)
            possible_return_value = self.array_bucket[new_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1
            print("???", retrieval_collisions)

    def print_hash_table(self):
        print(self.array_bucket)


my_hash_table = HashTable(8)

