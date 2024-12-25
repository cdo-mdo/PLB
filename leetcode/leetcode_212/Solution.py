class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [0]*n
        min_price = prices[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i - 1] - min_price)
            min_price = min(min_price, prices[i])

        return dp[-1]

solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
