class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = {}
        starts = defaultdict(int)
        
        for n in nums:
            d[n] = 0
        
        for n in nums:
            if n - 1 not in d:
                starts[n] = 1

        for k in starts.keys():
            kk = k
            while True:
                kk += 1
                if kk in d:
                    starts[k] += 1
                else:
                    break
        if len(starts.values()) > 0:
            return max(starts.values())
        else:
            return 0                  
