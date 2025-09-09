def peopleAwareOfSecret(n, delay, forget):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[1] = 1
    shareable = 0

    for d in range(2, n + 1):
        start = d - delay
        if start >= 1:
            shareable = (shareable + dp[start]) % MOD

        stop = d - forget
        if stop >= 1:
            shareable = (shareable - dp[stop]) % MOD

        dp[d] = shareable

    ans = 0
    for d in range(max(1, n - forget + 1), n + 1):
        ans = (ans + dp[d]) % MOD

    return ans
