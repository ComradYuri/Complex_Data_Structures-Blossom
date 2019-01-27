from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    # instantiation creates an array with a LinkedList at each index for the array
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        # creates node that will be inserted the linkedList at the array index
        payload = Node([key, value])

        list_at_array = self.array[array_index]
        # for loop iterates through list and overwrites values if there is a key match.
        # It then returns as otherwise the code would continue and insert another node.
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                return
        # inserts payload into linked list
        list_at_array.insert(payload)

    def retrieve(self, key):
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        list_at_index = self.array[array_index]
        # iterates through linkedlist searching for matching keys
        for item in list_at_index:
            if key == item[0]:
                return item[1]
        return None


blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])
print(blossom.retrieve("daisy"))
