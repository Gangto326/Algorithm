import sys

N, K = map(int, sys.stdin.readline().split())
string = ""

for _ in range(N-K):
    string += "a"

for i in range(K):
    string += chr(97+i)

print(string)