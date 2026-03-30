class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        i = m - 1
        j = n - 1

        for x in range(m + n - 1, -1 , -1):
            if j < 0:
                break
            elif i >= 0 and nums1[i] > nums2[j]:
                nums1[x] = nums1[i]
                nums1[i] = 0 
                i = i - 1
            else:
                nums1[x] = nums2[j]
                j = j - 1

        return 

        