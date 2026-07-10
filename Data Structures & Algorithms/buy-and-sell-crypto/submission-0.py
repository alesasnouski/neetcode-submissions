class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = prices[0]
        for p in prices[1:]:
            if p < min_p:
                min_p = p
            elif p > min_p and (p - min_p) > profit:
                profit = p - min_p
        return profit