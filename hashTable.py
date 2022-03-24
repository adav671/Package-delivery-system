# HashTable class using chaining.
#This is the self-adjusting data structure I am using that will allow me
#to store, lookup, remove, and insert packages in the system
#Big O notation: is generally O(1) for Hash tables. Worst case scenario is O(n)

class HashTable:
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=41):
        # initialize the hash table
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

        #insert/update item in the bucket that will grab all the package's info

    def insert(self, key, item):
        bucket = hash(key)% len(self.table)
        bucket_list = self.table[bucket]

        #update key (that's already in bucket)
        for pp in bucket_list:
            if pp[0]==key:
                pp[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    #search for package and be able to display the package's info
    def lookup(self, key):
        #get bucket list
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        #print(bucket_list)

        for pp in bucket_list:
            if pp[0]==key:
                return pp[1]
            return None



    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for pp in bucket_list:
            if pp[0] == key:
                bucket_list.remove([pp[0], pp[1]])

