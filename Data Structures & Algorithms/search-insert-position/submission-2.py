class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums)
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if mid + 1 > n - 1:
                    return mid + 1
                elif nums[mid + 1] > target:
                    return mid + 1
                left = mid + 1
            else:
                if mid - 1 < 0:
                    return 0
                elif nums[mid - 1] < target:
                    return mid
                right = mid - 1
        return -1