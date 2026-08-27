class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        cnt=0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[cnt]=nums[i]
                cnt+=1
        return cnt