class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n]+=1
        sorted_freq = dict(sorted(freq.items(), key=lambda item: -item[1]))
        return list(sorted_freq.keys())[:k]
        


