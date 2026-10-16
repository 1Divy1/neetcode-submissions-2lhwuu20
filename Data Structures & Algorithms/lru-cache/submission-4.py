class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity
        self.ops = []

    def get(self, key: int) -> int:
        res = self.store.get(key, -1)
        if res != -1:
            self.ops.remove(key)
            self.ops.append(key)
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
            self.ops.remove(key)
            self.ops.append(key)
        elif len(self.store) == self.capacity:
            poppedKey = self.ops.pop(0)
            self.store.pop(poppedKey)  # pop the least recently used key
            self.store[key] = value
            self.ops.append(key)
        else:
            self.store[key] = value
            self.ops.append(key)