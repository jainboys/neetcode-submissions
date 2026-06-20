class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
              return ""

        def is_match(l,r):
            for c in t:
                if fw[c]<ft[c]:
                    return False
            return True

        res=""
        ft = defaultdict(int)
        fw = defaultdict(int)
        for c in t:
            ft[c]+=1
        l = 0

        for r in range(len(s)):
            fw[s[r]]+=1
            

            while(l<r and fw[s[l]] > ft[s[l]]):
                # slide from left and shrink
                fw[s[l]]-=1
                l+=1
            if r-l+1 >= len(t) and is_match(l,r) and (not res or (r-l+1)<len(res)):
                res = s[l:r+1]

            #current_window is the answer if match
            
        return res



        