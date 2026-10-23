class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        import heapq
        max_heap=[]
        for key,val in freq.items():
            heapq.heappush(max_heap,(-val,key))
        result=[]
        for _ in range(k):   
            result.append(heapq.heappop(max_heap)[1])
        return result
        