class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        if len(nums) == 0:
            return 0
        max_cnt = 0
        
        for i in hash_set:
            if (i - 1) not in hash_set:
                length = 1

                while i + length in hash_set:
                    length = length + 1

                max_cnt = max(length, max_cnt)


        return max_cnt

            