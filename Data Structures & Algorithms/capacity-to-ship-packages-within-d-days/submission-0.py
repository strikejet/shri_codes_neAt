class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The capacity must be at least the maximum element. otherwise we won't be able to load the maximum weight

        maxi = sum(weights)
        mini = max(weights)

        while mini <= maxi:
            mid = (mini + maxi)//2

            curr_weight = 0
            days_used = 1

            for w in weights:
                if curr_weight + w > mid:
                    days_used = days_used + 1
                    curr_weight = w
                else:
                    curr_weight = curr_weight + w
            
            if days_used > days:
                mini = mid + 1
            else:
                maxi = mid - 1
        return mini