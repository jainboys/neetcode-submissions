class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mem = {}
        res = 0
        for i in range(len(heights)):
            j = i+1
            while j < len(heights) and j > i:
                if (i,j) in mem:
                    continue
                else:
                    cur_water = (j-i) * min(heights[i], heights[j])
                    mem[(i,j)] = cur_water
                
                if cur_water > res:
                    res = cur_water
                j+=1
        return res
