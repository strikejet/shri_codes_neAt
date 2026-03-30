class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cntr = Counter(nums)
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                cntr[nums[i]] = cntr[nums[i]] - 1
                cntr[nums[j]] = cntr[nums[j]] - 1
                balance = nums[i] + nums[j]
                target = -balance
                if target in cntr and cntr[-balance] > 0:
                    triplet = tuple(sorted([nums[i], nums[j], target]))
                    ans.add(triplet)
                cntr[nums[i]] = cntr[nums[i]] + 1
                cntr[nums[j]] = cntr[nums[j]] + 1                
        return list(ans)