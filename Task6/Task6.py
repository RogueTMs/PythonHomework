class LRUCache:

    def __init__(self, capacity=16):
        self.cap = capacity
        self.cash = {}
        self.hist = []

    def put(self, key, value):
        if len(self.cash) == self.cap:
            self.cash.pop(self.hist.pop(0))

        self.hist.append(key)
        self.cash[key] = value

    def get(self, key):
        if self.cash.get(key):
            self.hist.pop(0)
            self.hist.append(key)
        return self.cash.get(key)
