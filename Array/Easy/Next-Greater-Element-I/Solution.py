class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n=len(nums2)
        ans=[-1]*n
        stk=[]

        for i in range(n-1,-1,-1):
            while stk and stk[-1] <= nums2[i]:
                stk.pop()
            if stk:
                ans[i]=stk[-1]
            stk.append(nums2[i])
        ng={}
        for i in range(n):
            ng[nums2[i]]=ans[i]
        res=[]
        for num in nums1:
            res.append(ng[num])
        return res