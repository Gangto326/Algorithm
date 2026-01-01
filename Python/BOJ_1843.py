import sys

def solve():
    N = int(sys.stdin.readline().rstrip())

    A_count = 0
    for i in range(1, N//2 + 1):
        y_count = N - i*2

        if y_count > 0:
            A_count += y_count
        else:
            break

    print(A_count)

    B_count = 0
    num_set = set()
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            num_set.add(i)
            num_set.add(N // i)

    num_list = sorted(list(num_set))
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            if (num_list[i] + num_list[j]) in num_set:
                B_count += 1
            elif num_list[i] + num_list[j] > N:
                break

    print(B_count)

    C_count = 0
    eratos = [True] * (N+1)

    for i in range(2, int(N**0.5)+1):
        if not eratos[i]:
            continue

        num = i * i
        while num <= N:
            eratos[num] = False
            num += i

    for i in range(3, N+1):
        if eratos[i] and i + 2 <= N:
            if eratos[i + 2]:
                C_count += 1

    print(C_count)


if __name__ == "__main__":
    solve()