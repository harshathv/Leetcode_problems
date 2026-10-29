class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_current=nums[0]
        max_upto=nums[0]
        for num in range(1,len(nums)):
            max_current=max(nums[num],max_current+nums[num])
            max_upto=max(max_current,max_upto)
        return max_upto
        