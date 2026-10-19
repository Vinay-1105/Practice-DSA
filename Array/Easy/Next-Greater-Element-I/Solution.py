class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stk=[]
        for i in nums1:
            next_greater=-1
            target_found=False

            for j in nums2:
                if j==i:
                    target_found=True
                elif target_found:
                    if j>i:
                        next_greater=j
                        break
            stk.append(next_greater)
        return stk