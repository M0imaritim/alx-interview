#!/usr/bin/python3
"""Efficient DP solution to the coin change problem."""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given total."""
    if total <= 0:
        return 0
    if not coins:
        return -1

    unique_coins = sorted(set(coin for coin in coins if 0 < coin <= total),
                          reverse=True)
    if not unique_coins:
        return -1

    if unique_coins[0] == total:
        return 1

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in unique_coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] < total + 1:
                new_count = dp[amount - coin] + 1
                if new_count < dp[amount]:
                    dp[amount] = new_count

    return dp[total] if dp[total] <= total else -1
