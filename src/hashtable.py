# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hash = self._hash(key)
        index = hash % self.capacity
        if self.storage[index] != None and not isinstance(self.storage[index], LinkedPair):
            pair = LinkedPair(key, value)
            pair2 = LinkedPair(None, self.storage[index])
            pair.next = pair2
            self.storage[index] = pair
            pass
        if isinstance(self.storage[index], LinkedPair):
            pair = LinkedPair(key, value)
            pair2 = self.storage[index]
            pair.next = pair2
            self.storage[index] = pair
        self.storage[index] = value



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash = self._hash(key)
        index = hash % self.capacity
        if self.storage[index] == None:
            print("key not found")
            pass
        value = self.storage[index]
        if isinstance(self.storage[index], LinkedPair) and self.storage[index].next != None:
            value = self.storage[index].value
            self.storage[index] = self.storage[index].next

        self.storage.pop(index=index)
        return value


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash = self._hash(key)
        index = hash % self.capacity
        value = None
        if isinstance(self.storage[index], LinkedPair):
            pair = self.storage[index]
            while pair.key != key and pair.next != None:
                pair = pair.next
            value = pair.value
        else:
            value = self.storage[index]
            print(value)
        return value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        newCapacity = self.capacity * 2
        newArray = [None] * newCapacity
        for i in range(self.capacity):
            value = self.storage[i]
            newArray[i] = value
        self.storage = newArray
        self.capacity = newCapacity
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
