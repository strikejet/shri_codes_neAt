class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_num = nums[0]
        cnt = 0
        for i in nums:

            if i == max_num:
                max_num = i
                cnt = cnt + 1
            else:
                cnt = cnt - 1
                if cnt == 0:
                    max_num = i
                    cnt = 1
        return max_num
