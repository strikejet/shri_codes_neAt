class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0 , 0
        n = len(nums)
        prefix_sum = [0] * n

        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        i, j = 0, 0
        minimal_length = n + 1

        for j in range(n):
            # shrink window while valid
            while i <= j:
                curr_sum = prefix_sum[j] if i == 0 else prefix_sum[j] - prefix_sum[i - 1]

                if curr_sum >= target:
                    minimal_length = min(minimal_length, j - i + 1)
                    i += 1
                else:
                    break

        
        return 0 if minimal_length == (n + 1) else minimal_length