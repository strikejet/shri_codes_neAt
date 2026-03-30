class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for x in range(0,len(nums)):
            pos[nums[x]] = x
        
        for y in range(0,len(nums)):
            if (target - nums[y]) in pos:
                if y == pos[target - nums[y]]:
                    continue
                else:
                    return [y, pos[target - nums[y]]] 
        