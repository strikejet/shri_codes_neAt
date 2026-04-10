class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 1
        maxi = max(piles)

        while mini <= maxi:
            mid = (mini + maxi)//2
            time = 0
            for i in piles:
                t = i // mid
                r = i % mid
                if r > 0:
                    t = t + 1
                time = time + t
            
            if time > h:
                mini = mid + 1
            else:
                maxi = mid - 1
            
        return mini
