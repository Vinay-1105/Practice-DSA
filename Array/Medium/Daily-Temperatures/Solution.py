class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                idx=stack.pop()
                ans[idx]=i-idx
            stack.append(i)
        return ans