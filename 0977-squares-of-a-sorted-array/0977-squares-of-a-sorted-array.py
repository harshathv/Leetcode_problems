class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans=[]
        for num in nums:
            k=num*num
            ans.append(k)
            ans.sort()
        return ans
        