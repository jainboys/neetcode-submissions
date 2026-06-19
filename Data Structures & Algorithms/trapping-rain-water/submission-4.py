class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 1, len(height)-2
        ml, mr = height[0], height[len(height)-1]
        while l<=r:
            if ml<=mr:
                res+=max(0, ml-height[l])
                ml = max(ml, height[l])
                l+=1
            else:
                res+=max(0, mr-height[r])
                mr=max(mr, height[r])
                r-=1
        return res


