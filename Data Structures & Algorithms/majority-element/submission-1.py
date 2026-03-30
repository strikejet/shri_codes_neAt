class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        target = maxcount = 0
        for i in nums:
            count[i] = count[i] + 1
            if count[i] > maxcount:
                target = i
                maxcount = count[i]

        return target