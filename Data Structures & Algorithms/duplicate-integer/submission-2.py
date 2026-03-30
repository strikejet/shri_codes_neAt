class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a_set = set(nums)
        return len(nums) != len(a_set)
