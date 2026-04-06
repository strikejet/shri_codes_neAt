class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_set = set()

        for i in nums:
            if i not in hash_set:
                hash_set.add(i)
            elif i in hash_set:
                hash_set.remove(i)
        if len(hash_set) == 1:   
            return hash_set.pop()