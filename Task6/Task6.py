class LRUCache:

    def __init__(self, capacity=16):
        self.cap = capacity
        self.cash = {}
        self.pop = []

    def put(self, key, value):
        if len(self.cash) == self.cap:
            self.cash.pop(self.pop.pop(0))

        self.pop.append(key)
        self.cash[key] = value

    def get(self, key):
        if self.cash.get(key):
            self.pop.pop(key)
            self.pop.append(key)
        return self.cash.get(key)
