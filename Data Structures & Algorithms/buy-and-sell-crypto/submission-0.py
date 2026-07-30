class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0
        R=1
        max_profit=0
        current_profit=0

        while R<len(prices):
            if prices[L]<prices[R]:
                current_profit=prices[R]-prices[L]
                max_profit=max(current_profit,max_profit)
            else:
                L=R
            R+=1

        return max_profit

            
            
