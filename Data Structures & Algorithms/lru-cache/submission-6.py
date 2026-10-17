class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self.__remove(node)
        self.__insertMRU(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.__remove(node)
            self.__insertMRU(node)
        else:
            if len(self.cache) == self.capacity:
                self.__deleteLRU()
            node = Node(key, value)
            self.__insertMRU(node)
            self.cache[key] = node

    # PRIVATE HELPERS
    def __remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def __deleteLRU(self) -> None:
        lru = self.head.next
        self.__remove(lru)
        del self.cache[lru.key]

    def __insertMRU(self, node) -> None:
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node