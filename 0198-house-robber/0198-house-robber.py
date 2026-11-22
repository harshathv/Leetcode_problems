class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1,rob2=0,0
        n=len(nums)
        for i in range(n):
            temp=max(rob1+nums[i],rob2)
            rob1=rob2
            rob2=temp
        return rob2
        