
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        highs = []
        res = [0 for x in range(len(temperatures))]

        for (i, t) in enumerate(temperatures):
            if not highs or highs[-1][0] > t:
                highs.append((t, i))
            else:
                j = len(highs) - 1
                while highs and highs[j][0] < t: 
                    el = highs.pop()
                    j = j - 1
                    res[el[1]] = i - el[1]
                highs.append((t, i))
        return res            
