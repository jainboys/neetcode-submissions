class Solution:
    res = 1
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sequence = {}
        def find(x):
            if sequence[x][0] == x:
                return sequence[x]
            else:
                return find(sequence[x][0])
        
        def union(x, y):
            sx = find(x)
            sy = find(y)
            if sx and sy:
                sy[0] = x
                sx[1]=sx[1]+sy[1]
                if sx[1]> self.res:
                    self.res = sx[1]

        for i in nums:
            if i in sequence:
                continue
            sequence[i] = [i, 1]
            for x in (i-1, i+1):
                if x in sequence:
                    union(x, i)
        return self.res
    
    

