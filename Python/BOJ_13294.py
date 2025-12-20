import sys

MOD = 1_000_000_007

N = int(sys.stdin.readline()) % MOD

facto = 1
i = 1
while True:
    facto = facto * i % MOD
    
    if facto == N:
        print(i)
        break

    i += 1