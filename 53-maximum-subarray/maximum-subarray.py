class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            current=nums[i]
            old_max=max_sum
            max_sum=max(current,current+old_max)
            ans=max(ans,max_sum)
        return ans
