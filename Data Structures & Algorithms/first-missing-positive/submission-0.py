class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positives = []
        for i in nums:
            if i > 0:
                positives.append(i)
        
        positives = set(positives)
        for i in range(1, len(positives)+1):
            if i not in positives:
                return i
        return len(positives) + 1