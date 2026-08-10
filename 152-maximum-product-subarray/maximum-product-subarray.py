class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        min_prod=nums[0]
        ans=nums[0]

        for i in range(1,len(nums)):
            current=nums[i]
            old_max=max_prod
            old_min=min_prod
            max_prod=max(current,current*old_max,current*old_min)
            min_prod=min(current,current*old_max,current*old_min)

            ans=max(ans,max_prod)
        return ans

