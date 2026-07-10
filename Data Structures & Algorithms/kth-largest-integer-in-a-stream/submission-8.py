class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        from collections import defaultdict
        self.k = k
        self.nums = nums
        self.maxEl = max(nums) if nums else None
        self.minEl = min(nums) if nums else None
        self.d = defaultdict(list)
        for k in nums:
            self.d[k].append(k)

    def add(self, val: int) -> int:
        self.maxEl = max(self.maxEl, val) if self.maxEl is not None else val
        self.minEl = min(self.minEl, val) if self.minEl is not None else val
        self.d[val].append(val)
        k = 0
        for x in range(self.maxEl, self.minEl - 1, -1):
            k = k + len(self.d[x])
            if k >= self.k:
                return x

