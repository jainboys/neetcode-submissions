class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            j = i+1
            while j < len(heights) and j > i:
                cur_water = (j-i) * min(heights[i], heights[j])
                if cur_water > res:
                    res = cur_water
                j+=1
        return res
