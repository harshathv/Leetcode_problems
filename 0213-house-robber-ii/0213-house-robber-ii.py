class Solution:
    def rob(self, nums: list[int]) -> int:
        def get_max(nums):
            rob1,rob2=0,0
            for i in range(len(nums)):
                temp=max(rob1+nums[i],rob2)
                rob1=rob2
                rob2=temp
            return rob2
        return max(get_max(nums[:-1]),get_max(nums[1:]),nums[0])
