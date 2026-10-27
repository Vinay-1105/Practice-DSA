class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=0 #to iterate in the first arr
        p2=0 #to iterate in the second arr
        final_arr=[]

        while p1<m and p2<n:
            if nums1[p1]<nums2[p2]:
                final_arr.append(nums1[p1])
                p1+=1
            else:
                final_arr.append(nums2[p2])
                p2+=1
            
        print(p1)
        print(p2)
        print(final_arr)
        while p1<m:
            final_arr.append(nums1[p1])
            p1 += 1
        while p2<n:
            final_arr.append(nums2[p2])
            p2 +=1 
        print(final_arr)
        for i in range(len(final_arr)):
            nums1[i]=final_arr[i]