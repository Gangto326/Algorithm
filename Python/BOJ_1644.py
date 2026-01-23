import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    eratos = [True] * (N+1)
    num_list = []

    for i in range(2, N+1):
        if eratos[i]:
            num_list.append(i)
            for j in range(i * i, N+1, i):
                eratos[j] = False

    answer = 0
    total = 0
    left = 0
    right = 0
    lenght = len(num_list)

    while True:
        if total >= N:
            if total == N:
                answer += 1

            total -= num_list[left]
            left += 1
        
        elif right == lenght:
            break

        else:
            total += num_list[right]
            right += 1
    
    print(answer)


if __name__ == "__main__":
    solve()