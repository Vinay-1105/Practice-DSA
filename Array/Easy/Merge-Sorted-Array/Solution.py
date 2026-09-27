class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=0
        p2=0
        arr=[]
        while p1<m and p2<n:
            if nums1[p1]<nums2[p2]:
                arr.append(nums1[p1])
                p1+=1
            else:
                arr.append(nums2[p2])
                p2+=1
        print(p1)
        print(p2)
        print(arr)
        while p1<m:
            arr.append(nums1[p1])
            p1+=1
        while p2<n:
            arr.append(nums2[p2])
            p2+=1
        print(arr)
        for i in range(len(arr)):
            nums1[i] = arr[i]