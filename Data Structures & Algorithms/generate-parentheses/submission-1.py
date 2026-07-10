class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        def pairs(acc):
            if len(acc[0]) == 2 * n:
                return acc
            newacc = []
            for a in acc:
                left = a.count('(')
                right = a.count(')')
                if left < n:
                    newacc.append(a + '(')
                if right < left:
                    newacc.append(a + ')')
            return pairs(newacc)
        
        return pairs(['('])

