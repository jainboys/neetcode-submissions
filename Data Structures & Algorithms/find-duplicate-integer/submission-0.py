class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(32):
            bi = 1<<i
            x = 0
            for num in nums:
                bit_set = num & bi
                if bit_set:
                    x +=1
            y = 0
            for num in range(n):
                bit_set = num & bi
                if bit_set:
                    y +=1
            
            if x > y:
                res = res | bi
        return res




        