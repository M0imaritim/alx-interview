#!/usr/bin/python3
"""Efficient DP solution to the coin change problem."""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given total."""
    if total <= 0:
        return 0
    if not coins:
        return -1

    coins = [coin for coin in coins if coin <= total]
    if not coins:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
