class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        max_prof = 0
        for i in range(1, len(prices)):
            if prices[i]>cur_min:
                max_prof=max(max_prof, prices[i]-cur_min)
            else:
                cur_min = min(cur_min, prices[i])
        return max_prof



