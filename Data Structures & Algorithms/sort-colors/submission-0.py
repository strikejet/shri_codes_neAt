class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_ind = i
            for j in range(i + 1, len(nums)):  # FIX
                if nums[j] < nums[min_ind]:
                    min_ind = j

            nums[i], nums[min_ind] = nums[min_ind], nums[i]
        return

        
        