class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        stack = [] # pair (start of rectangle, height of rectangle)
        # stack will store the starting point of a rectangle with a height
        for i, h in enumerate(heights):
            start=i
            while(stack and stack[-1][1] >= h):
                start, hp = stack.pop()
                maxArea = max(maxArea, (hp * (i-start)))
            stack.append((start, h))
        print(stack)
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, h*(n-i))
        return maxArea
        

