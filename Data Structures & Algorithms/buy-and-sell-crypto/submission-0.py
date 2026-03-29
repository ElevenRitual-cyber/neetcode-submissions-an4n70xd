class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        temp=prices[0]
        for i in range(1,len(prices)):
            today=prices[i]
            if temp>today:
                temp=today
                continue
            else:
                p=today-temp
            profit=max(profit,p)
        return profit
        