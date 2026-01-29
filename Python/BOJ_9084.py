import sys

def solve():
    read = sys.stdin.readline
    T = int(read().rstrip())

    for tc in range(T):
        N = int(read().rstrip())
        coin_list = list(map(int, read().split()))
        target = int(read().rstrip())
        DP = [0] * (target+1)
        DP[0] = 1

        for coin in coin_list:
            for i in range(coin, target+1):
                DP[i] += DP[i-coin]
        
        print(DP[-1])


if __name__ == "__main__":
    solve()