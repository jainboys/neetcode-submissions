class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        max_len=0
        fmax=0
        res = 0
        f = defaultdict(int)
        for r in range(len(s)):
            f[s[r]] +=1
            fmax = max(fmax, f[s[r]])
            while (r-l+1)-fmax>k:
                f[s[l]]-=1
                fmax = max(fmax, f[s[l]])
                l+=1
            res = max(res, (r-l+1))
        return res

