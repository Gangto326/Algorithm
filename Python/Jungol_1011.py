import sys

def solve():
    read = sys.stdin.readline()
    N, M, K = map(int, read.split())

    eratos = [True] * (M + 1)
    eratos[0] = False
    eratos[1] = False

    for i in range(2, M + 1):
        if eratos[i]:
            for j in range(i + i, M + 1, i):
                eratos[j] = False

    answer = 0
    for i in range(K + 1, M + 1, N):
        if eratos[i]:
            answer += 1
    
    print(answer)


if __name__ == "__main__":
    solve()