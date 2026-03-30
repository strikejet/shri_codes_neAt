class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = set(nums)
        x, y = None, None
        for i in range(len(nums)):
            if (target - nums[i]) in hash_map:
                y = i
                x = nums.index(target - nums[i])
        return [x, y]