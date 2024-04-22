class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def _next_index(self, index):
        return (index + 1) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = self._next_index(index)
        self.keys[index] = key
        self.values[index] = value

    def retrieve(self, key):
        index = self._hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._next_index(index)
        return None

    def exists(self, key):
        index = self._hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = self._next_index(index)
        return False


if __name__=='__main__':
    
    obj = HashTable(5)
    obj.insert("thor", 4)
    obj.insert("ironman", 3)
    obj.insert("hulk", 2)
    print(obj.retrieve("thor"))  
    print(obj.retrieve("ironman"))  
    print(obj.retrieve("hulk"))  
    print(obj.exists("thor")) 
    print(obj.exists("antman")) 
