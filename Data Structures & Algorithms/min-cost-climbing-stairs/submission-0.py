class Solution:
    # [1, 2, 3]
    # min_cost[0] = 0
    # min_cost[1] = min(cost[0], cost[1])
    # min_cost[2] = 0, 
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if cost is None:
            return 0
        n = len(cost)
        min_cost = [0] * (n+1)
        min_cost[1] = 0

        for i in range(2, n + 1):
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2])
        return min_cost[n]
