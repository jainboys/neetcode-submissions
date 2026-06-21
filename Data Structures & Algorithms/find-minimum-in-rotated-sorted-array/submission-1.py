class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        res = 999999999999999
        while l<=r:
            mid = l+(r-l)//2
            if nums[l]<=nums[mid]:
                res = min(res, nums[l])
                l = mid+1
            else:
                res = min(res, nums[mid])
                r = mid-1
        
        return res

