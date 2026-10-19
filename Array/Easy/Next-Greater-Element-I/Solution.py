class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater=defaultdict(lambda:-1)
        stack=[]

        for i in nums2:
            while stack and stack[-1] < i:
                next_greater[stack.pop()]=i
            stack.append(i)
        return [next_greater[i] for i in nums1]