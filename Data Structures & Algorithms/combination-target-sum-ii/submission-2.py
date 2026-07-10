class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()

        def combs(i, lst):
            lst_sum = sum([candidates[x] for x in lst])
            if lst_sum == target and len(set(lst)) == len(lst):
                res = [candidates[x] for x in lst]
                res.sort()
                result.add(tuple(res))
            if i >= len(candidates) or lst_sum >= target:
                return
            lst.append(i)

            combs(i, lst)
            lst.pop()
            combs(i + 1, lst)
        
        combs(0, [])
        
        return [list(x) for x in result]