class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resset = set()
        for (i, n0) in enumerate(nums):
            for (j, n1) in enumerate(nums):
                for (k, n2) in enumerate(nums):
                    if i != j and j != k and i != k and n0 + n1 + n2 == 0: 
                        lst = [str(x) for x in sorted([n0, n1, n2])]
                        resset.add(",".join(lst))

        resl = []
        for x in resset:
            subel = []
            for el in x.split(','):
                subel.append(int(el))
            resl.append(subel)
        return resl
      