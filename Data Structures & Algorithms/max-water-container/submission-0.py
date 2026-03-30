class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_vol = min(heights[i], heights[j]) * (j-i) 
        while i < j:
            if heights[i] < heights[j]:
                i = i + 1
                if heights[i] > heights[i-1]:
                    vol = min(heights[i], heights[j]) * (j-i)
                    max_vol = max(max_vol, vol)
            elif heights[j] < heights[i]:
                j = j - 1
                if heights[j] > heights[j+1]:
                    vol = min(heights[i], heights[j]) * (j-i)
                    max_vol = max(max_vol, vol)
            else:
                i = i + 1
                j = j - 1
                vol = min(heights[i], heights[j]) * (j-i)
                max_vol = max(max_vol, vol)
            
            
        return max_vol
