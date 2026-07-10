class LRUCache:
    from collections import deque
    def __init__(self, capacity: int):
        self.storage = {}
        self.dqueue = deque(maxlen=capacity)
        

    def get(self, key: int) -> int:
        if self.storage.get(key):
            try:
                self.dqueue.remove(key)
                self.dqueue.append(key)
            except ValueError:
                self.storage.pop(key)
        return self.storage.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if self.storage.get(key):
            try:
                self.dqueue.remove(key)
            except ValueError:
                pass
        self.storage[key] = value
        self.dqueue.append(key)
        
