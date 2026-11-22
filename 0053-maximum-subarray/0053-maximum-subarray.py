class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
       if not nums:
        return 0
       max_current=nums[0]
       max_far=nums[0]
       for i in range(1,len(nums)):
        max_current=max(nums[i],max_current+nums[i])
        max_far=max(max_far,max_current)
       return max_far
        