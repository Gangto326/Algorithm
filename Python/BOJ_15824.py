import sys

read = sys.stdin.readline
N = int(read())

MOD = 1_000_000_007
menu_list = sorted(list(map(int, read().split())))
double_list = [0] * 300_010

double_num = 1
for i in range(300010):
    double_list[i] = double_num - 1
    double_num *= 2
    double_num %= MOD

answer = 0
for i in range(N-1, -1, -1):
    answer += (menu_list[i] * double_list[i]) % MOD
    answer -= (menu_list[i] * double_list[N-i-1]) % MOD
    answer %= MOD

print(answer)