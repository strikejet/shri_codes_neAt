class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ls = []
        for i in cnt:
            if cnt[i] > len(nums)/3:
                ls.append(i)
        return ls