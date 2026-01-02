import sys

read = sys.stdin.readline
N, K = map(int, read().split())
num_list = list(map(int, read().split()))


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    
    return a


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    
    return (a * b) // gcd(a, b)


answer = 0
for i in range(1, 1 << K):
    count = 0
    lcm_num = 1

    for j in range(K):
        if i & (1 << j) != 0:
            count += 1
            lcm_num = lcm(lcm_num, num_list[j])
        
    if lcm_num > N:
        continue

    if count % 2 == 0:
        answer -= N // lcm_num
    else:
        answer += N // lcm_num

print(N - answer)