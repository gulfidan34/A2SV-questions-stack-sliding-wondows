class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        price = [0, 0]
        for i in range(2, len(cost)):
            price.append(min(price[i - 1] + cost[i - 1], price[i - 2] + cost[i - 2]))
        return min(price[-1] + cost[-1], price[-2] + cost[-2])