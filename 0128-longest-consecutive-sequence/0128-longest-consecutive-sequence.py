class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n=set(nums)
        longest=0
        for num in n:
            if num-1 not in n:
                curr=num
                curr_longest=1
                while curr+1 in n:
                    curr+=1
                    curr_longest+=1
                longest=max(longest,curr_longest)
        return longest

            


        