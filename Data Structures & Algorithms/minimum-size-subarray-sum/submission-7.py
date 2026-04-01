class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0 
        n = len(nums)
        minimal_len = n + 1
        total = 0
        for right in range(n):
            total = total + nums[right]
            while total >= target:
                minimal_len = min(right - left + 1, minimal_len)
                total = total - nums[left]
                left = left + 1
            
        return 0 if minimal_len == (n + 1) else minimal_len
