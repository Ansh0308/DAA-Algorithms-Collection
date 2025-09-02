def minCoins(coins, n): 
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    coins_used = []
    i = n
    while i > 0:
        for coin in coins:
            if i - coin >= 0 and dp[i] == dp[i - coin] + 1:
                coins_used.append(coin)
                i -= coin
                break
    return str(len(coins_used))+" = "+str(coins_used)

coins=[1,5,6,8]
n=11
print(minCoins(coins,n))