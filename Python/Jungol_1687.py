import sys

def solve():
    read = sys.stdin.read().split()
    if not read:
        return
        
    N = int(read[0])
    cows = "".join(read[1:N+1])

    answer = ""
    left = 0
    right = N - 1

    while left <= right:
        if cows[left:right + 1] < cows[left:right + 1][::-1]:
            answer += cows[left]
            left += 1
        else:
            answer += cows[right]
            right -= 1

    for i in range(0, N, 80):
        print(answer[i:i + 80])
        

if __name__ == "__main__":
    solve()