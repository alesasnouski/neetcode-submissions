class MinStack:

    def __init__(self):
        self.l = []
        self.m = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if self.m:
            mmin = min(val, self.m[-1])
            self.m.append(mmin)
        else:
            self.m.append(val)    

    def pop(self) -> None:
        self.m.pop()
        return self.l.pop()
        

    def top(self) -> int:
        if self.l:
            return self.l[-1]
        else:
            return None    

    def getMin(self) -> int:
        if self.m:
            return self.m[-1]
        else:
            return None    
        
