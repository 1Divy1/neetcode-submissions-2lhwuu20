class TimeMap:

    def __init__(self):
        self.store = {}  # {key: [(value, timestamp)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key, [])
        res = ""

        l, r = 0, len(pairs) - 1
        while l <= r:
            m = (l + r) // 2
            if pairs[m][1] > timestamp:
                r = m - 1
                continue
            res = pairs[m][0]
            l = m + 1

        return res