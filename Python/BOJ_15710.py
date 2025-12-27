import sys

MOD = 1_000_000_007
read = sys.stdin.readline
a, b, n = map(int, read().split())

print(pow(pow(2, 31, MOD), n-1, MOD))