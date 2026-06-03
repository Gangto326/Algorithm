def solution(n):
    MOD = 1000000007
    count = [0, 1, 3, 10, 23, 62, 170] + [0] * n
    
    for i in range(7, n + 1):
        count[i] = (count[i - 1] + 2 * count[i - 2] + 6 * count[i - 3] + count[i - 4] - count[i - 6]) % MOD
        
    return count[n]