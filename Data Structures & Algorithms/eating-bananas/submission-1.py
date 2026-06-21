class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours(speed):
            hrs = 0
            for p in piles:
                hrs+=(-(-p//speed))
            return hrs


        l = 1
        r = max(piles)
        res=99999999999999
        while l<=r:
            mid = l+(r-l)//2
            cur_hrs = get_hours(mid)
            print(f'{l}-{r}-{mid}-{cur_hrs}')
            if cur_hrs<=h:
                res=min(res, mid)
                r=mid-1
            else:
                l=mid+1
        return res

