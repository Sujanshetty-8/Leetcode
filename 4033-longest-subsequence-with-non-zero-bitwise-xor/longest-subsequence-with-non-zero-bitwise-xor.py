class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total=0
        non_zero=False

        for num in nums:
            total^=num
            if num!=0:
                non_zero=True
        if not non_zero:
            return 0
        return len(nums) if total!=0 else len(nums)-1