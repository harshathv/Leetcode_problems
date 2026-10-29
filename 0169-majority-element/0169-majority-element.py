class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        m=0
        c=0
        for num in nums:
            if c==0:
                m=num
            if m==num:
                c+=1
            else:
                c-=1
        return m