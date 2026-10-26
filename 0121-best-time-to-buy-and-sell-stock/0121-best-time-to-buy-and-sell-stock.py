class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        min_price=prices[0]
        for price in prices:
            if price<min_price:
                min_price=price
            temp=price-min_price
            if temp>max_price:
                max_price=temp
        return max_price
        