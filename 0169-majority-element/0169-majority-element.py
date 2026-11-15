class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap={}
        n=0
        maj=0
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
            if hashmap[num]>maj:
                maj=hashmap[num]
                n=num
        return n