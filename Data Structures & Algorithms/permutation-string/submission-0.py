class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_match(l, r):
            if r-l+1 != len(s1):
                return False
            for c in s1:
                if s1_count[c] != s2_count[c]:
                    return False
            return True

        l = 0
        s1_count = defaultdict(int)
        for i in range(len(s1)):
            s1_count[s1[i]]+=1

        s2_count = defaultdict(int)
        for r in range(len(s2)):
            s2_count[s2[r]]+=1

            while(r-l+1>len(s1)):
                s2_count[s2[l]]-=1
                l+=1
            if is_match(l,r):
                return True
        return False
