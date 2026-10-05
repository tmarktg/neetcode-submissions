class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        bestP = 0

        def swap(i, j):
            tmp = prices[i]
            prices[i] = prices[j]
            prices[j] = tmp

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                bestP = max(diff, bestP)
            else:
                l = r
            
            r +=1

        return bestP
