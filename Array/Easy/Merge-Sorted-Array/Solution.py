class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # first we will get the last 
        # index of nums1
        # last = m+n-1
        # # merge in reverse order
        # while m > 0 and n > 0:
        #     if nums1[m-1] > nums2[n-1]:
        #         nums1[last] = nums1[m-1]
        #         m -= 1
        #     else:
        #         nums1[last] = nums2[n-1]
        #         n -= 1
        #     last -= 1
        
        # # fill nums1 with leftover nums2
        # while n > 0:
        #     nums1[last] = nums2[n-1]
        #     n = n-1
        #     last = last-1
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()