table_size = 10
hash_table = [None] * table_size  # List to hold key-value pairs

def hash_function(key, table_size):
    return key % table_size

def insert_with_linear_probing(key, value):
    hash_value = hash_function(key, table_size)
    initial_hash = hash_value
    while hash_table[hash_value] is not None:
        hash_value = (hash_value + 1) % table_size
        if hash_value == initial_hash:
            raise Exception("Hash table is full")
    hash_table[hash_value] = (key, value)

keys = [12, 45, 67, 91, 23, 8, 18]  # Additional keys added to induce collisions

# Insert key-value pairs into the hash table using linear probing to handle collisions
for key in keys:
    insert_with_linear_probing(key, "value")

# Print the hash table to see where each key-value pair is stored
print(hash_table)
