import heapq
from collections import defaultdict
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        nums = defaultdict(int)
        for t in tasks:
            nums[t] += 1
        tlen = len(tasks)
        res = []
        while tlen > 0:
            cont = []
            keys = sorted(nums.keys(), key=lambda x: nums[x], reverse=True)
            for k in keys:
                if nums[k] > 0 and len(cont) < n + 1:
                    cont.append(k)
                    nums[k] -= 1
                    tlen -= 1
            while len(cont) < n + 1:
                if tlen == 0:
                    break
                cont.append("Idle")
            res += cont
        print(res)
        return len(res)



            

        