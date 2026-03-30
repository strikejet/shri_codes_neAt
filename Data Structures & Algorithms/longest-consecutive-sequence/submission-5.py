class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest=0

        for num in s:
            if num -1 not in s:
                next_num = num + 1
                lenght=1
                while next_num in s:
                    lenght+=1
                    next_num+=1
                    
                longest=max(longest,lenght)
        return longest

            