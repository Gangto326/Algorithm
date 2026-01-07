import sys

read = sys.stdin.readline
N, K = map(int, read().split())

if 2 * N > K:
    print(-1)
elif 2 * N == K:
    print((2 * (N-1)) + 1)
else:
    print(2 * N)