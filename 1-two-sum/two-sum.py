class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''

        dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return [dict[complement], i] 
            dict[num] = i
        return [-1, -1]