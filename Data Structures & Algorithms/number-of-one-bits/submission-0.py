class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in bin(n):
            print(i)
            if i == '1':
                cnt += 1
        return cnt