class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # arr = [[]] * len(nums)
        # This creates multiple references to the SAME list

        # 👉 So:

        # arr[1].append(5)

        # will also modify:

        # arr[2], arr[3], arr[4]...

        # 💥 Everything gets corrupted
        cntr = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        for c in cntr:
            arr[cntr[c]].append(c)
        ans = []
        for i in range(len(nums), 0, -1):
            if arr[i] != []:
                ans.extend(arr[i])
            if len(ans) >= k:
                break
        return ans
        
                