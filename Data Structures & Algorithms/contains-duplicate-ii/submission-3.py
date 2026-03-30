class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 1
        hash_set = {nums[i]}
        if len(nums) < 2:
            return False

        while j <= i + k:
            if nums[j] in hash_set:
                return True
            else:
                hash_set.add(nums[j])
                j = j + 1 
        
        while j < len(nums):
            hash_set.remove(nums[i])
            i = i + 1
            if nums[j] in hash_set:
                return True
            else:
                hash_set.add(nums[j])
                j = j + 1 
        
        return False


