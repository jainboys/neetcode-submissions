class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        i = 0
        nums = sorted(nums)
        for i in range(0, len(nums)-2):
            j = i+1
            k = len(nums)-1
            while i < j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if (nums[i], nums[j], nums[k]) not in seen:
                        res.append([nums[i], nums[j], nums[k]])
                    seen.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1
        return res
