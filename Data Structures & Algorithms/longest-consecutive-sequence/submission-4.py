class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        if len(nums) == 0:
            return 0
        possible_seq_starts = []
        for i in nums:
            if (i - 1) not in hash_set:
                possible_seq_starts.append(i)
        max_cnt = 1
        

        for i in possible_seq_starts:
            j = i + 1
            cnt = 1
            while j in hash_set:
                j = j + 1
                cnt = cnt + 1
                if max_cnt < cnt:
                    max_cnt = cnt

        return max_cnt

            