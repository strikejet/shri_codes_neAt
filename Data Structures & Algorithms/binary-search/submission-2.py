class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] > target or nums[right] < target:
                return -1
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid

        return -1
