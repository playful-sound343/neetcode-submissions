class MyHashMap:
    def __init__(self):
        # 1. Base array size locked to a prime number to naturally distribute hashes
        self.capacity = 10007
        # 2. Build 10,007 physically independent bucket lists in RAM
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key: int) -> int:
        # 3. The GPS: Converts any numeric key into a valid array index (0 to 10006)
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # 4. Check if the key already exists on this rack. If yes, update it.
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        
        # 5. If it's a completely new key, bind it as a [key, value] packet and add it
        bucket.append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # 6. Look at the label (pair[0]) of each box. Return the content (pair[1]) if it matches.
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
                
        # 7. Default safety net if the key was never stored
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # 8. Keep track of the index position (i) while scanning the contents (pair)
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                # 9. Physically wipe out the box at this exact row position
                bucket.pop(i)
                return  # Exit instantly so we don't look any further
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)