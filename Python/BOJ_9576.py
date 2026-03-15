import sys

def solve():
    read = sys.stdin.readline
    T = int(read())

    for ts in range(T):
        N, M = map(int, read().split())
        books = [True] * (N + 1)
        answer = 0

        query_list = []

        for _ in range(M):
            start, end = map(int, read().split())
            query_list.append((start, end))

        query_list.sort(key = lambda x: (x[1], x[0]))

        for start, end in query_list:
            for i in range(start, end + 1):
                if books[i]:
                    books[i] = False
                    answer += 1
                    break
        
        print(answer)


if __name__ == "__main__":
    solve()