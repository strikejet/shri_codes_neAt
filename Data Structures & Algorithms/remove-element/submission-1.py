class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Return k, such that the first k elements of nums contain the elements not equal to val.
        # The elements beyond k do not matter.
        k = 0   # index for placing valid elements
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
# # If you insist on popping, you must pop from right to left:
#         count = 0
#         indexes = []
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 count = count + 1
#             else:
#                 indexes.append(i)
#         for i in range(len(indexes)):
#             indexes[i] = indexes[i] - 1

#         for i in indexes:
#             nums.pop(i)
#         return count

# two pointer approach - 
