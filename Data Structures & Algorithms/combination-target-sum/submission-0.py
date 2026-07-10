class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def combs(i, lst):
            if sum(lst) == target:
                result.append(lst.copy())
            if i >= len(candidates) or sum(lst) >= target:
                return
            lst.append(candidates[i])

            combs(i, lst)
            lst.pop()
            combs(i + 1, lst)
        
        combs(0, [])
        
        return result