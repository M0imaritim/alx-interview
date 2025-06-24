#!/usr/bin/python3
"""0x0A-primegame - Prime Game."""


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x < 1:
        return None

    n = max(nums)

    # Sieve of Eratosthenes
    is_prime = [False, False] + [True for _ in range(2, n + 1)]
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    # Precompute number of primes up to each index
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(len(prime_count)):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
