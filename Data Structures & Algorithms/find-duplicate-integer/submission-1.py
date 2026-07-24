class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(32):
            bi = 1<<i
            x = y = 0
            for num in nums:
                if num & bi:
                    x +=1
            for num in range(n):
                if num & bi:
                    y +=1
            
            if x > y:
                res = res | bi
        return res




        