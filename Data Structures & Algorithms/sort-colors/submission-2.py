class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, n - 1
        k = 0 
        while k <= j:

            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i = i + 1
                k = k + 1
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j = j - 1
            else:
                k = k + 1

        return
