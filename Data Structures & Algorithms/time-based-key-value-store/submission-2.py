class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.m = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        else:
            mp = self.m[key]
            result = ""
            for i in range(timestamp, 0, -1):
                if i in mp:
                    result = mp[i]
                    break
            return result        
