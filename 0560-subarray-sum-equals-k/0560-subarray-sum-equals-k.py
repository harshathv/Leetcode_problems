class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={}
        hashmap[0]=1
        running_sum=0
        matching=0
        for n in nums:
            running_sum+=n
            if running_sum-k in hashmap:
                matching+=hashmap[running_sum-k]
            if running_sum in hashmap:
                hashmap[running_sum]+=1
            else:
                hashmap[running_sum]=1
        return matching