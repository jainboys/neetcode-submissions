import heapq
# class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     res = []
    #     h = []
    #     for i in range(len(nums)):
    #         heapq.heappush(h, (-nums[i], i))
    #         if i >= (k-1):
    #             while h[0][1] < (i-k):
    #                 heapq.heappop(h)
    #             res.append(-h[0][0])
    #     return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output
      