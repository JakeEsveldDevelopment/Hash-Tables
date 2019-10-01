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
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            pair = LinkedPair(key, value)
            pair2 = self.storage[index]
            pair.next = pair2
            self.storage[index] = pair
            return
        self.storage[index] = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] == None:
            print("key not found")
            return
        pair = self.storage[index]
        previous = None
        while True:
            if pair.next is None:
                removedValue = pair.value
                if previous != None:
                    previous.next = None
                else:
                    self.storage[index] = None
                return removedValue
            if pair.key == key:
                removedValue = pair.value
                if pair.next != None and previous != None:
                    previous.next = pair.next
                elif previous != None:
                    previous.next = None
                else:
                    self.storage[index] = None
                return removedValue
            previous = pair
            pair = pair.next           


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.

        '''

        index = self._hash_mod(key)
        if self.storage[index] != None:
            pair = self.storage[index]
            while True:
                if pair.next is None:
                    return pair.value
                if pair.key == key:
                    return pair.value
                pair = pair.next
            
        return self.storage[index]

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_capacity = self.capacity
        self.capacity *= 2
        oldStorage = self.storage
        self.storage = [None] * self.capacity
        for i in range(old_capacity):
            if oldStorage[i] != None:
                pair = oldStorage[i]
                while True:
                    self.insert(pair.key, pair.value)
                    if pair.next != None:
                        pair = pair.next
                        continue
                    else:
                        break
                    



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
