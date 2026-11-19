class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0

        profit = 0

        while right < len(prices):
            profit = max(prices[right] - prices[left], profit)

            right += 1
            if right < len(prices) and prices[right] <= prices[left]:
                left = right
            
        return profit


            