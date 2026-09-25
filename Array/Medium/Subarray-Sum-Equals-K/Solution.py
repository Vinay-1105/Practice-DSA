class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # # brute force approach
        # n=len(nums)
        # cnt=0
        # for i in range(n):
        #     sum=0
        #     for j in range(i, n):
        #         sum+=nums[j]
        #         if sum==k:
        #             cnt+=1
        # return cnt

        # better approach
        cnt=0
        prefix_sum=0
        prefix_cnt={0:1}

        for num in nums:
            prefix_sum+=num
            cnt+=prefix_cnt.get(prefix_sum-k, 0)
            prefix_cnt[prefix_sum] = prefix_cnt.get(prefix_sum,0)+1
        return cnt
