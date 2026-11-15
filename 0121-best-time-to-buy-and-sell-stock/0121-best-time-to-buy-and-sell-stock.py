class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        min_price=float("inf")
        for n in prices:
            if n<min_price:
                min_price=n
            max_price=max(max_price,n-min_price)
        return max_price
        