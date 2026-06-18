class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        rt = [1] * length
        res = [0] * length
        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]
        for i in range(length-2, -1, -1):
            rt[i] = rt[i+1] * nums[i+1]
        
        print(left)
        print(rt)
        for i in range(length):
            res[i] = left[i] * rt[i]
        return res
