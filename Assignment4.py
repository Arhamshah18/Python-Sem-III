# Top-Down Approach (Memoization)
def fib_memoization(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

# Bottom-Up Approach (Tabulation)
def fib_tabulation(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Driver Code
n = 10
print(f"Fibonacci({n}) using Memoization: {fib_memoization(n)}")
print(f"Fibonacci({n}) using Tabulation:  {fib_tabulation(n)}")
