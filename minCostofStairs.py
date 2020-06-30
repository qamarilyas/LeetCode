
def minCostClimbingStairs(cost):
    for i in range(2,len(cost)):
        cost[i]+=min(cost[i-1],cost[i-2])
    return min(cost[len(cost)-1],cost[len(cost)-2])

x=cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(x))