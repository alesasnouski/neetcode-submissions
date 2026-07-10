class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        res = []
        for n in nums:
            d[n] += 1
        for x in range(k):
            for (k, v) in d.items():
                if v == max(d.values()):
                    res.append(k)
                    d.pop(k)
                    break
        return res                