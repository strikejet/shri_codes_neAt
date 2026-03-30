class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int) # Prefix Sum occurred -> count of the prefix sum
        prefix_map[0] = 1 # base case ()
        curr_sum = 0
        cnt = 0
        for i in nums:
            curr_sum += i
            diff = curr_sum - k
            cnt += prefix_map.get(diff, 0)
            prefix_map[curr_sum] = 1 + prefix_map.get(curr_sum, 0)

        return cnt