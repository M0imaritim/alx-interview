#!/usr/bin/python3
"""Coin Change Problem: Find minimum number of coins to make a given total."""


def makeChange(coins, total):
    """Determine the minimum number of coins needed to make a given total."""
    if total <= 0:
        return 0
    if not coins:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
