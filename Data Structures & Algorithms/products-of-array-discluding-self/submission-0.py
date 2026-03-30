class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        if nums.count(0) > 1:
            return [0] * len(nums)
        elif nums.count(0) == 1:
            ind = nums.index(0)
            ls = [0] * len(nums)
            for i in nums:
                if i != 0:
                    total_product *= i
            ls[ind] = total_product
            return ls 
        for i in nums:
            total_product *= i

        return [int(total_product / x) for x in nums]