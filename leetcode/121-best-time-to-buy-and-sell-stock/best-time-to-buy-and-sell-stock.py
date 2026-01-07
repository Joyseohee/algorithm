class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        low_idx, max_profit = -1, -1
        
        for i, p in enumerate(prices):
            if low_idx == -1 or prices[low_idx] > p:
                low_idx = i
            
            curr_profit = p - prices[low_idx]
            max_profit = max(max_profit, curr_profit)

        return max_profit