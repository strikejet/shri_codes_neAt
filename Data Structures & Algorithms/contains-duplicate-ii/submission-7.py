class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0 
        right = 1
        hash_set = {nums[0]}
        while right < len(nums):
            
            while right - left > k:
                hash_set.remove(nums[left])
                left += 1

            # then check
            if nums[right] in hash_set:
                return True

            hash_set.add(nums[right])
            right = right + 1

        return False
            


            