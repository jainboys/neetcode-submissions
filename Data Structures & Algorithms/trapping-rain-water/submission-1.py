class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = [0] * len(height)
        right = [0] * len(height)
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i-1])
        for j in range(len(height)-2, 0, -1):
            right[j] = max(right[j+1], height[j+1])
        print(left)
        print(right)
        for i in range(1, len(height)-1):
            if left[i] <= height[i] or right[i] <= height[i]:
                continue
            else:
                res+=min(left[i], right[i])-height[i]
        return res


