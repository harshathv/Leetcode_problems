class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n  
        stk = []  

    # Traverse the array from right to left
        for i in range(2*n - 1, -1, -1):
            idx=i%n

        # Pop elements from the stack that are less 
        # than or equal to the current element
            while stk and nums[stk[-1]] <= nums[idx]:
                stk.pop()

        # If the stack is not empty, the element at the 
        # top of the stack is the next greater element
            if stk:
                res[idx] = nums[stk[-1]]

        # Push the current index onto the stack
            stk.append(idx)

        return res

        