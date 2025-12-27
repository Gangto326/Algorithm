import sys

read = sys.stdin.readline
N, K = map(int, read().split())
string_list = list(read().rstrip())

left = 0
right = N-1
while 0 < K and left < right:
    while string_list[left] != 'C' and left < right:
        left += 1
    
    while string_list[right] != 'P' and left < right:
        right -= 1
    
    if string_list[left] == 'C' and string_list[right] == 'P':
        string_list[right] = 'C'
        string_list[left] = 'P'
        K -= 1

P_count = [0] * (N+1)
answer = 0
for i in range(1, N+1):
    if string_list[i-1] == 'P':
        P_count[i] = P_count[i-1] + 1
    else:
        P_count[i] = P_count[i-1]

for i in range(N):
    if string_list[i] == 'C':
        answer += (P_count[i+1] * (P_count[i+1]-1)) // 2

print(answer)