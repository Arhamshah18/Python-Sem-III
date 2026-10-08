# 1. Top-Down Approach (Memoization)
def knapsack_top_down(weights: list, values: list, capacity: int, n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n == 0 or capacity == 0:
        return 0
    if (n, capacity) in memo:
        return memo[(n, capacity)]

    if weights[n - 1] <= capacity:
        include = values[n - 1] + knapsack_top_down(weights, values, capacity - weights[n - 1], n - 1, memo)
        exclude = knapsack_top_down(weights, values, capacity, n - 1, memo)
        memo[(n, capacity)] = max(include, exclude)
    else:
        memo[(n, capacity)] = knapsack_top_down(weights, values, capacity, n - 1, memo)

    return memo[(n, capacity)]

# 2. Bottom-Up Approach (Tabulation)
def knapsack_bottom_up(weights: list, values: list, capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Driver Code
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(f"Max Value (Top-Down):  {knapsack_top_down(weights, values, capacity, len(values))}")
print(f"Max Value (Bottom-Up): {knapsack_bottom_up(weights, values, capacity)}")
